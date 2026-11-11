#!/usr/bin/env python3
"""Collect a live snapshot of SKStacks + SKPatch + skaegis status from the public GitHub API.

Used by both a local run (to seed data/status.json with real numbers before the
first commit) and the `status` GitHub Actions workflow (hourly refresh). Reads
only public endpoints via the `gh` CLI, which honors GH_TOKEN/GITHUB_TOKEN when
present and otherwise falls back to the anonymous public rate limit. No secret
beyond the default Actions token is required.

Never invents a number: if a source call fails (for example, a repo with no
releases yet), the field is set to null rather than guessed.
"""
import base64
import datetime
import json
import re
import subprocess
import sys

DASH_MAP = str.maketrans({chr(0x2014): "-", chr(0x2013): "-"})


def clean(value):
    """Strip em/en dashes out of any text pulled from an external source."""
    if value is None:
        return None
    return value.translate(DASH_MAP)


def gh_json(path):
    out = subprocess.run(
        ["gh", "api", path], capture_output=True, text=True, check=True
    )
    return json.loads(out.stdout)


def gh_raw_file(repo, path, ref="main"):
    out = subprocess.run(
        ["gh", "api", f"repos/{repo}/contents/{path}?ref={ref}", "-q", ".content"],
        capture_output=True,
        text=True,
        check=True,
    )
    return base64.b64decode(out.stdout.strip()).decode("utf-8")


def latest_release(repo):
    try:
        r = gh_json(f"repos/{repo}/releases/latest")
    except subprocess.CalledProcessError:
        return None
    return {"tag": clean(r.get("tag_name")), "published_at": r.get("published_at")}


def open_pr_count(repo):
    r = gh_json(f"search/issues?q=repo:{repo}+type:pr+state:open")
    return r["total_count"]


def last_ci_main(repo):
    r = gh_json(f"repos/{repo}/actions/runs?branch=main&per_page=1")
    runs = r.get("workflow_runs") or []
    if not runs:
        return None
    run = runs[0]
    return {
        "workflow": clean(run.get("name")),
        "conclusion": run.get("conclusion"),
        "at": run.get("created_at"),
    }


def changelog_top_heading(repo):
    try:
        text = gh_raw_file(repo, "CHANGELOG.md")
    except subprocess.CalledProcessError:
        return None
    for line in text.splitlines():
        if line.startswith("## "):
            return clean(line[3:].strip())
    return None


def parse_pinned_images(repo):
    """Parse the 'At a glance' table of docs/v1-service-catalog.md."""
    try:
        text = gh_raw_file(repo, "docs/v1-service-catalog.md")
    except subprocess.CalledProcessError:
        return []
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Service | Tier"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        if line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        name_md, tier, _what, upstream = cells[0], cells[1], cells[2], cells[3]
        m = re.match(r"\[([^\]]+)\]", name_md)
        name = m.group(1) if m else name_md
        rows.append(
            {
                "service": clean(name),
                "tier": clean(tier),
                "pinned_upstream": clean(upstream),
            }
        )
    return rows


def parse_policy_lanes(repo):
    """Parse the 'Cadence and policy' table of docs/skpatch-program.md."""
    try:
        text = gh_raw_file(repo, "docs/skpatch-program.md")
    except subprocess.CalledProcessError:
        return []
    rows = []
    in_table = False
    for line in text.splitlines():
        if line.startswith("| Finding | Lane"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        if line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        rows.append({"finding": clean(cells[0]), "lane": clean(cells[1])})
    return rows


def main():
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    data = {
        "generated_at": now,
        "skstacks": {
            "repo": "smilinTux/skstacks",
            "latest_release": latest_release("smilinTux/skstacks"),
            "changelog_top_heading": changelog_top_heading("smilinTux/skstacks"),
            "open_pull_requests": open_pr_count("smilinTux/skstacks"),
            "ci_main": last_ci_main("smilinTux/skstacks"),
        },
        "skpatch": {
            "repo": "smilinTux/skpatch",
            "latest_release": latest_release("smilinTux/skpatch"),
            "open_pull_requests": open_pr_count("smilinTux/skpatch"),
            "ci_main": last_ci_main("smilinTux/skpatch"),
        },
        "skpatch_site": {
            "repo": "smilinTux/skpatch-skworld-io",
            "open_pull_requests": open_pr_count("smilinTux/skpatch-skworld-io"),
            "ci_main": last_ci_main("smilinTux/skpatch-skworld-io"),
        },
        "skaegis": {
            "repo": "smilinTux/skaegis",
            "latest_release": latest_release("smilinTux/skaegis"),
            "open_pull_requests": open_pr_count("smilinTux/skaegis"),
            "ci_main": last_ci_main("smilinTux/skaegis"),
        },
        "skaegis_site": {
            "repo": "smilinTux/skaegis-skworld-io",
            "open_pull_requests": open_pr_count("smilinTux/skaegis-skworld-io"),
            "ci_main": last_ci_main("smilinTux/skaegis-skworld-io"),
        },
        "pinned_images": parse_pinned_images("smilinTux/skstacks"),
        "policy_lanes": parse_policy_lanes("smilinTux/skstacks"),
    }
    json.dump(data, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
