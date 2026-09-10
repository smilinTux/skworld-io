import data, html, datetime
L = data.LAYERS
N = sum(len(x[3]) for x in L)
TODAY = datetime.date.today().isoformat()

nav = "\n".join(
 f'      <a href="#{k}">{html.escape(t)}</a>' for k,t,s,_ in L)

def card(slug, name, blurb):
    return (f'        <a class="pcard" href="https://{slug}.skworld.io/">\n'
            f'          <span class="pname">{html.escape(name)}</span>\n'
            f'          <span class="pblurb">{html.escape(blurb)}</span>\n'
            f'          <span class="phost">{slug}.skworld.io</span>\n'
            f'        </a>')

layers = []
for i,(k,title,sub,items) in enumerate(L, start=1):
    cards = "\n".join(card(*it) for it in items)
    layers.append(f'''    <section class="layer" id="{k}">
      <div class="lhead">
        <span class="lnum">{i:02d}</span>
        <div>
          <h2>{html.escape(title)}</h2>
          <p class="lsub">{html.escape(sub)}</p>
        </div>
        <span class="lcount">{len(items)}</span>
      </div>
      <div class="pgrid">
{cards}
      </div>
    </section>''')
LAYERS_HTML = "\n\n".join(layers)

HTML = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SKWorld: Sovereign AI Infrastructure, Silicon to Soul</title>
<meta name="description" content="SKWorld is a sovereign AI stack you own end to end: identity and post-quantum security, infrastructure, memory, communications, agents, and soul. {N} open projects across 7 layers. Your data, your keys, your hardware. Walk away any time and it all comes with you.">
<meta name="keywords" content="sovereign AI, self-hosted AI, AI infrastructure, agent framework, post-quantum, AI memory, soul blueprints, open source, SKWorld, smilinTux">
<link rel="canonical" href="https://skworld.io/">

<meta property="og:type" content="website">
<meta property="og:url" content="https://skworld.io/">
<meta property="og:title" content="SKWorld: Sovereign AI Infrastructure, Silicon to Soul">
<meta property="og:description" content="{N} open projects across 7 layers. Identity, infrastructure, memory, comms, agents, soul. Own the whole vertical. No rented middle, no black-box bottom.">
<meta property="og:image" content="https://skworld.io/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:site_name" content="SKWorld">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@smilinTux">
<meta name="twitter:title" content="SKWorld: Sovereign AI Infrastructure, Silicon to Soul">
<meta name="twitter:description" content="{N} open projects across 7 layers. Own the whole vertical. Your data, your keys, your hardware.">
<meta name="twitter:image" content="https://skworld.io/og-image.png">
<meta name="twitter:image:alt" content="SKWorld, sovereign AI infrastructure from silicon to soul">

<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>%F0%9F%90%A7</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600;12..96,800&family=Public+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="style.css">

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "SKWorld",
  "url": "https://skworld.io/",
  "description": "Sovereign AI infrastructure. An owned stack from identity and post-quantum security through infrastructure, memory, communications, agents, and soul.",
  "sameAs": ["https://github.com/smilinTux"]
}}
</script>
</head>
<body>

<header class="hero">
  <div class="inner">
    <div class="topbar">
      <span class="brand">&#128039; SKWORLD</span>
      <nav class="topnav">
        <a href="#stack">The stack</a>
        <a href="#pillars">Why</a>
        <a href="https://github.com/smilinTux">GitHub &#8599;</a>
      </nav>
    </div>
    <span class="eyebrow">{N} open projects &middot; 7 layers &middot; one owned vertical</span>
    <h1>From silicon to soul.<br>Own the whole stack.</h1>
    <p class="sub">Every layer of an AI stack, built to be owned rather than rented. Your data, your keys, your hardware. Walk away any time and all of it comes with you.</p>
    <div class="cta">
      <a class="btn primary" href="#stack">Explore the stack</a>
      <a class="btn ghost" href="https://github.com/smilinTux">Read the source</a>
    </div>
  </div>
</header>

<div class="inner">

  <section id="pillars" class="pillars">
    <div class="pill">
      <span class="pico">&#128301;</span>
      <h3>First principles</h3>
      <p>We did not accept the default stack. Every layer was questioned and rebuilt: open, swappable, yours. No lock-in baked in by default.</p>
    </div>
    <div class="pill">
      <span class="pico">&#11014;&#65039;</span>
      <h3>The full vertical</h3>
      <p>From silicon to soul, you own every layer. No rented middle, no black-box bottom. One cohesive stack, not a bag of services you depend on.</p>
    </div>
    <div class="pill">
      <span class="pico">&#128274;</span>
      <h3>Data sovereignty</h3>
      <p>Your data is yours, cryptographically and physically. It never leaves your control, and leaving is always possible.</p>
    </div>
  </section>

  <div class="stackhead" id="stack">
    <h2>The stack</h2>
    <p>Ordered the way it is built: the floor first, the soul last. Every project is open source and runs on hardware you control.</p>
    <nav class="layernav">
{nav}
    </nav>
  </div>

{LAYERS_HTML}

  <section class="closing">
    <h2>Start anywhere</h2>
    <p>Nothing here requires the rest. Take one layer, one project, one binary. The stack is designed so that adopting a piece never obliges you to adopt the whole, and never obliges you to stay.</p>
    <div class="cta">
      <a class="btn primary" href="https://skos.skworld.io/">Start with SKOS</a>
      <a class="btn ghost" href="https://skcapstone.skworld.io/">Or SKCapstone</a>
    </div>
  </section>

  <footer>
    <p class="fmain">SKWorld is built in the open by <a href="https://github.com/smilinTux">smilinTux</a>. Sovereign infrastructure for people who would rather own than rent.</p>
    <p class="fmeta"><a href="https://github.com/smilinTux">github.com/smilinTux</a> &middot; <a href="https://skresearch.skworld.io/">Research</a> &middot; <a href="https://skrsi.skworld.io/">How we measure ourselves</a> &middot; Apache-2.0</p>
  </footer>

</div>
</body>
</html>
'''
open("../index.html","w").write(HTML)

SITEMAP = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
           f'  <url><loc>https://skworld.io/</loc><lastmod>{TODAY}</lastmod>'
           f'<changefreq>weekly</changefreq><priority>1.0</priority></url>']
for k,t,s,items in L:
    for slug,_,_ in items:
        SITEMAP.append(f'  <url><loc>https://{slug}.skworld.io/</loc>'
                       f'<lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq>'
                       f'<priority>0.7</priority></url>')
SITEMAP.append('</urlset>')
open("../sitemap.xml","w").write("\n".join(SITEMAP)+"\n")
print(f"index.html: {sum(1 for _ in open("../index.html"))} lines")
print(f"sitemap.xml: {N+1} urls")
