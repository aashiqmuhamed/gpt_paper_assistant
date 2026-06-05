"""Render the papers/ archive into a polished static HTML site (dist/).

Stdlib only — no dependencies. Design language mirrors aashiqmuhamed.github.io
(al-folio "earthy editorial" palette: Spectral serif + Lato sans, light/dark).

Usage: python3 render_html.py [--papers-dir papers] [--out dist]
"""

import argparse
import html
import json
import re
from pathlib import Path
from string import Template

ABSTRACT_PREFIX = re.compile(r"^arXiv:\S+\s+Announce Type:\s*\S+\s*Abstract:\s*", re.I)
CRITERION_RE = re.compile(r"criteri(?:on|a)\s*#?\s*(\d+)", re.I)

PAGE = Template(
    """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Daily ArXiv Digest &mdash; $date</title>
<meta name="description" content="Personalized daily arXiv paper digest: $npapers papers selected for $date.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;0,700;1,400&family=Lato:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #ffffff;
    --card-bg: #fafaf8;
    --text: #1c2845;
    --text-light: #555c70;
    --accent: #3d67c0;
    --link: #577BAF;
    --terra: #ac4f36;
    --mustard: #e3b658;
    --green: #3a7d5e;
    --border: rgba(28, 40, 69, 0.12);
    --chip-bg: rgba(61, 103, 192, 0.08);
    --shadow: 0 1px 3px rgba(28, 40, 69, 0.06);
    --shadow-hover: 0 4px 14px rgba(28, 40, 69, 0.10);
  }
  html[data-theme="dark"] {
    --bg: #1a1d23;
    --card-bg: #22252b;
    --text: #d8d8dc;
    --text-light: #9a9aa3;
    --accent: #4c9a8f;
    --link: #7db8c9;
    --terra: #cd8f7c;
    --mustard: #e3b658;
    --green: #6fae8f;
    --border: rgba(216, 216, 220, 0.14);
    --chip-bg: rgba(76, 154, 143, 0.12);
    --shadow: 0 1px 3px rgba(0, 0, 0, 0.25);
    --shadow-hover: 0 4px 14px rgba(0, 0, 0, 0.4);
  }
  * { box-sizing: border-box; }
  body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family: "Spectral", "Iowan Old Style", Georgia, serif;
    font-size: 16px;
    line-height: 1.6;
    transition: background 0.25s ease, color 0.25s ease;
  }
  a { color: var(--link); text-decoration: none; }
  a:hover { color: var(--accent); text-decoration: underline; }
  .wrap { max-width: 880px; margin: 0 auto; padding: 0 20px 80px; }

  /* ---------- masthead ---------- */
  header { padding: 48px 0 12px; border-bottom: 2px solid var(--text); }
  .kicker {
    font-family: "Lato", -apple-system, sans-serif;
    font-size: 12px; font-weight: 700;
    letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--terra); margin: 0 0 6px;
  }
  h1 { font-size: 38px; font-weight: 700; margin: 0 0 4px; letter-spacing: -0.01em; }
  .masthead-meta {
    display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 18px;
    font-family: "Lato", -apple-system, sans-serif;
    font-size: 13.5px; color: var(--text-light); margin: 6px 0 18px;
  }
  .masthead-meta b { color: var(--text); font-weight: 700; }

  /* ---------- toolbar ---------- */
  .toolbar {
    position: sticky; top: 0; z-index: 10;
    display: flex; flex-wrap: wrap; align-items: center; gap: 10px;
    padding: 12px 0; margin-bottom: 26px;
    background: var(--bg);
    border-bottom: 1px solid var(--border);
    font-family: "Lato", -apple-system, sans-serif;
    transition: background 0.25s ease;
  }
  #search {
    flex: 1 1 220px; min-width: 160px;
    padding: 8px 12px; font-size: 14px; font-family: inherit;
    color: var(--text); background: var(--card-bg);
    border: 1px solid var(--border); border-radius: 8px; outline: none;
  }
  #search:focus { border-color: var(--accent); }
  .chip {
    padding: 7px 13px; font-size: 13px; font-weight: 700; font-family: inherit;
    color: var(--text-light); background: transparent;
    border: 1px solid var(--border); border-radius: 999px; cursor: pointer;
    transition: all 0.15s ease;
  }
  .chip:hover { border-color: var(--accent); color: var(--accent); }
  .chip.active { background: var(--accent); border-color: var(--accent); color: #fff; }
  select#archive {
    padding: 7px 10px; font-size: 13px; font-family: inherit; font-weight: 700;
    color: var(--text); background: var(--card-bg);
    border: 1px solid var(--border); border-radius: 8px; cursor: pointer;
  }
  #theme-toggle {
    width: 36px; height: 36px; font-size: 16px; line-height: 1;
    background: transparent; border: 1px solid var(--border); border-radius: 50%;
    cursor: pointer; color: var(--text);
  }
  #theme-toggle:hover { border-color: var(--accent); }
  #count { font-size: 13px; color: var(--text-light); margin-left: auto; }

  /* ---------- paper cards ---------- */
  .paper {
    position: relative;
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 20px 22px 16px 56px;
    margin-bottom: 16px;
    box-shadow: var(--shadow);
    transition: box-shadow 0.2s ease, transform 0.2s ease;
  }
  .paper:hover { box-shadow: var(--shadow-hover); transform: translateY(-1px); }
  .rank {
    position: absolute; left: 18px; top: 22px;
    font-family: "Lato", sans-serif; font-size: 13px; font-weight: 700;
    color: var(--text-light); opacity: 0.7;
  }
  .paper h2 { font-size: 19.5px; font-weight: 600; line-height: 1.35; margin: 0 0 6px; }
  .paper h2 a { color: var(--text); }
  .paper h2 a:hover { color: var(--accent); text-decoration: none; }
  .authors { font-style: italic; font-size: 14.5px; color: var(--text-light); margin: 0 0 10px; }
  .badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 10px;
            font-family: "Lato", sans-serif; }
  .badge {
    font-size: 11.5px; font-weight: 700; letter-spacing: 0.04em;
    padding: 3px 9px; border-radius: 999px;
  }
  .badge.rel { color: var(--accent); background: var(--chip-bg); }
  .badge.nov { color: var(--green); background: rgba(58, 125, 94, 0.10); }
  .badge.crit { color: var(--terra); background: rgba(172, 79, 54, 0.10); }
  .badge.match { color: #7a5c12; background: rgba(227, 182, 88, 0.25); }
  html[data-theme="dark"] .badge.match { color: var(--mustard); }
  .comment {
    font-size: 13.5px; color: var(--text-light); font-style: italic;
    border-left: 3px solid var(--mustard);
    padding: 2px 0 2px 10px; margin: 0 0 10px;
  }
  .abstract {
    font-size: 14.5px; color: var(--text-light); margin: 0 0 10px;
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical;
    overflow: hidden; cursor: pointer;
  }
  .paper.open .abstract { display: block; -webkit-line-clamp: unset; cursor: default; }
  .links { font-family: "Lato", sans-serif; font-size: 12.5px; font-weight: 700;
           letter-spacing: 0.06em; text-transform: uppercase; }
  .links a { margin-right: 14px; }
  .more {
    background: none; border: none; padding: 0; margin-right: 14px;
    font: inherit; color: var(--terra); cursor: pointer;
  }
  .more:hover { text-decoration: underline; }

  .empty { text-align: center; color: var(--text-light); padding: 60px 0; font-style: italic; }

  footer {
    margin-top: 56px; padding-top: 18px; border-top: 1px solid var(--border);
    font-family: "Lato", sans-serif; font-size: 13px; color: var(--text-light);
    display: flex; flex-wrap: wrap; gap: 8px 20px;
  }
  @media (max-width: 600px) {
    h1 { font-size: 28px; }
    .paper { padding-left: 22px; }
    .rank { position: static; display: inline-block; margin-bottom: 4px; }
  }
</style>
</head>
<body>
<div class="wrap">
  <header>
    <p class="kicker">Personalized arXiv scanner &middot; $categories</p>
    <h1>Daily ArXiv Digest</h1>
    <div class="masthead-meta">
      <span><b>$date_pretty</b></span>
      <span><b>$npapers</b> papers selected</span>
      <span>$nmatches author matches</span>
    </div>
  </header>

  <div class="toolbar">
    <input id="search" type="search" placeholder="Filter by title, author, abstract&hellip;" aria-label="Search papers">
    <button class="chip active" data-filter="all">All</button>
    <button class="chip" data-filter="rel5">R &ge; 5</button>
    <button class="chip" data-filter="nov5">N &ge; 5</button>
    <button class="chip" data-filter="match">Author match</button>
    <select id="archive" aria-label="Browse archive">$archive_options</select>
    <button id="theme-toggle" aria-label="Toggle dark mode">&#9789;</button>
    <span id="count"></span>
  </div>

  <main id="papers">
$cards
  </main>

  <footer>
    <span>Curated by <a href="https://github.com/aashiqmuhamed/gpt_paper_assistant">gpt_paper_assistant</a></span>
    <span><a href="https://aashiqmuhamed.github.io">aashiqmuhamed.github.io</a></span>
    <span>Scores: R = relevance, N = novelty (1&ndash;10, model-assigned)</span>
  </footer>
</div>

<script>
(function () {
  // ---------- theme ----------
  var root = document.documentElement;
  var saved = null;
  try { saved = localStorage.getItem("digest-theme"); } catch (e) {}
  var prefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
  setTheme(saved || (prefersDark ? "dark" : "light"));
  function setTheme(t) {
    root.setAttribute("data-theme", t);
    document.getElementById("theme-toggle").innerHTML = t === "dark" ? "&#9788;" : "&#9789;";
  }
  document.getElementById("theme-toggle").addEventListener("click", function () {
    var next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    setTheme(next);
    try { localStorage.setItem("digest-theme", next); } catch (e) {}
  });

  // ---------- filtering ----------
  var papers = Array.prototype.slice.call(document.querySelectorAll(".paper"));
  var chips = Array.prototype.slice.call(document.querySelectorAll(".chip"));
  var search = document.getElementById("search");
  var count = document.getElementById("count");
  var mode = "all";

  function apply() {
    var q = search.value.toLowerCase();
    var shown = 0;
    papers.forEach(function (p) {
      var okSearch = !q || p.getAttribute("data-search").indexOf(q) !== -1;
      var okMode =
        mode === "all" ? true :
        mode === "rel5" ? +p.getAttribute("data-rel") >= 5 :
        mode === "nov5" ? +p.getAttribute("data-nov") >= 5 :
        p.getAttribute("data-match") === "1";
      var ok = okSearch && okMode;
      p.style.display = ok ? "" : "none";
      if (ok) shown++;
    });
    count.textContent = shown + " / " + papers.length;
  }
  search.addEventListener("input", apply);
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      chips.forEach(function (x) { x.classList.remove("active"); });
      c.classList.add("active");
      mode = c.getAttribute("data-filter");
      apply();
    });
  });
  apply();

  // ---------- abstract expand ----------
  papers.forEach(function (p) {
    var toggle = function () { p.classList.toggle("open");
      var b = p.querySelector(".more");
      if (b) b.textContent = p.classList.contains("open") ? "Show less" : "Show more";
    };
    var abs = p.querySelector(".abstract");
    if (abs) abs.addEventListener("click", function () { if (!p.classList.contains("open")) toggle(); });
    var btn = p.querySelector(".more");
    if (btn) btn.addEventListener("click", toggle);
  });

  // ---------- archive nav ----------
  document.getElementById("archive").addEventListener("change", function () {
    if (this.value) window.location.href = this.value;
  });
})();
</script>
</body>
</html>
"""
)

CARD = Template(
    """    <article class="paper" data-search="$search" data-rel="$rel" data-nov="$nov" data-match="$match">
      <span class="rank">#$rank</span>
      <h2><a href="https://arxiv.org/abs/$arxiv_id">$title</a></h2>
      <p class="authors">$authors</p>
      <div class="badges">$badges</div>
$comment_html      <p class="abstract">$abstract</p>
      <div class="links">
        <button class="more">Show more</button>
        <a href="https://arxiv.org/abs/$arxiv_id">abs</a>
        <a href="https://arxiv.org/pdf/$arxiv_id">pdf</a>
      </div>
    </article>
"""
)


def esc(s):
    return html.escape(str(s), quote=True)


def pretty_date(iso):
    # 2026-06-04 -> June 4, 2026 (no datetime.strptime needed for tz safety)
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December",
    ]
    y, m, d = iso.split("-")
    return f"{months[int(m) - 1]} {int(d)}, {y}"


def render_card(rank, paper):
    title = esc(paper.get("title", "Untitled").strip())
    arxiv_id = esc(paper.get("arxiv_id") or paper.get("ARXIVID", ""))
    authors = ", ".join(paper.get("authors", []))
    abstract = ABSTRACT_PREFIX.sub("", paper.get("abstract", "")).strip()
    comment = (paper.get("COMMENT") or "").strip()
    rel = paper.get("RELEVANCE", "")
    nov = paper.get("NOVELTY", "")
    is_match = comment.lower() == "author match"

    badges = []
    if rel != "":
        badges.append(f'<span class="badge rel">R {esc(rel)}</span>')
    if nov != "":
        badges.append(f'<span class="badge nov">N {esc(nov)}</span>')
    for c in sorted(set(CRITERION_RE.findall(comment))):
        badges.append(f'<span class="badge crit">Criterion {esc(c)}</span>')
    if is_match:
        badges.append('<span class="badge match">Author match</span>')

    comment_html = ""
    if comment and not is_match:
        comment_html = f'      <p class="comment">{esc(comment)}</p>\n'

    search_blob = " ".join([title, authors, abstract]).lower()
    return CARD.substitute(
        rank=rank,
        arxiv_id=arxiv_id,
        title=title,
        authors=esc(authors),
        badges="".join(badges),
        comment_html=comment_html,
        abstract=esc(abstract),
        search=esc(search_blob),
        rel=esc(rel if rel != "" else -1),
        nov=esc(nov if nov != "" else -1),
        match="1" if is_match else "0",
    )


def render_page(date, papers, all_dates, categories, is_index):
    cards = "".join(render_card(i + 1, p) for i, p in enumerate(papers.values()))
    if not cards:
        cards = '    <p class="empty">No papers selected for this day.</p>'
    nmatches = sum(
        1 for p in papers.values() if (p.get("COMMENT") or "").lower() == "author match"
    )
    options = []
    for d in all_dates:  # newest first
        href = ("" if is_index else "../") + (
            "index.html" if d == all_dates[0] else f"archive/{d}.html"
        )
        if not is_index and d != all_dates[0]:
            href = f"{d}.html"
        sel = " selected" if d == date else ""
        options.append(f'<option value="{href}"{sel}>{pretty_date(d)}</option>')
    return PAGE.substitute(
        date=esc(date),
        date_pretty=esc(pretty_date(date)),
        npapers=len(papers),
        nmatches=nmatches,
        categories=esc(categories),
        archive_options="".join(options),
        cards=cards,
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers-dir", default="papers")
    ap.add_argument("--out", default="dist")
    args = ap.parse_args()

    # categories from config, best-effort
    categories = "cs.CL / cs.LG / cs.AI"
    try:
        import configparser

        cfg = configparser.ConfigParser()
        cfg.read("configs/config.ini")
        categories = " / ".join(
            c.strip() for c in cfg["FILTERING"]["arxiv_category"].split(",")
        )
    except Exception:
        pass

    papers_dir = Path(args.papers_dir)
    out = Path(args.out)
    (out / "archive").mkdir(parents=True, exist_ok=True)

    dates = sorted(
        (
            d.name
            for d in papers_dir.iterdir()
            if d.is_dir() and (d / "output.json").exists()
        ),
        reverse=True,
    )
    if not dates:
        raise SystemExit("No papers/<date>/output.json archives found.")

    for date in dates:
        with open(papers_dir / date / "output.json") as f:
            papers = json.load(f)
        page = render_page(date, papers, dates, categories, is_index=(date == dates[0]))
        target = (
            out / "index.html" if date == dates[0] else out / "archive" / f"{date}.html"
        )
        target.write_text(page, encoding="utf-8")
        # latest date also gets an archive copy so its dropdown entry never 404s
        if date == dates[0]:
            archive_copy = render_page(date, papers, dates, categories, is_index=False)
            (out / "archive" / f"{date}.html").write_text(archive_copy, encoding="utf-8")

    print(f"Rendered {len(dates)} day(s) -> {out}/ (latest: {dates[0]})")


if __name__ == "__main__":
    main()
