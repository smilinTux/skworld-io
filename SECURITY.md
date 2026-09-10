# Security Policy

This repository contains the **website only** for `skworld.io`. It holds no
application code, no credentials, and no runtime service.

## Reporting a vulnerability

Report privately through GitHub Security Advisories:

<https://github.com/smilinTux/skworld-io/security/advisories/new>

For a vulnerability in one of the linked projects, report it on that project's
own repository instead, so it reaches the people who own the code.

Please do not open a public issue for a security report.

## Scope

In scope here:

- Content that misstates a project's posture or capabilities.
- Leaked private paths, private host names, or credentials in published files.
- Site supply chain concerns, such as an unpinned or unexpected external asset.

Out of scope here, reportable on the project repositories instead:

- Behaviour, contracts, or vulnerabilities in any linked SKWorld project.

## Published assets

The page loads webfonts from `fonts.googleapis.com` and `fonts.gstatic.com`.
Everything else, including all CSS, is served from this origin. There is no
analytics, no tracker, and no third-party script.
