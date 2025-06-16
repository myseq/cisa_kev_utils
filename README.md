# CISA KEV & Utils

This repo hosts a daily GH action to scrape CISA's KEV catalogs including some utilities for CISA KEV.

|   | File | Description |
| - | ---- | ----------- |
| 1 | cisa_kev.json | Latest JSON |
| 2 | cisa_kev-old.json | Last-1 JSON |
| 3 | .github/workflows/scraper.yml | Daily scraper |
| 4 | kev-dashboard.py | See below |
| 5 | kev-catalog.py | See below |


## Archived Repos

This repos has consolidated from the following repos previously.

<dl>
  <dt>KEV-Dashboard</dt>
  <dd>This is a simple util that generates a dashboard for CISA's KEV.</dd>

  <dt>KEV-Catalog</dt>
  <dd>This util shows some catalogs, such as top-N vendors and top-N vulnerabile products, found in the CISA's KEV.</dd>

  <dt>CISA-Known-Exploited-Vulns</dt>
  <dd>This repo will run daily GH action to scrape CISA's KEV catalog and store in `docs/`.</dd>

</dl>


## MySeq Blog

 - <https://myseq.blogspot.com/2022/03/cisa-known-exploited-vuln-catalog.html>
 - <https://myseq.blogspot.com/2022/04/publish-kev-catalog-on-github.html>
 - <https://myseq.blogspot.com/2022/04/kev-dashboard.html>


## Links

 - [Termgraph](https://github.com/mkaz/termgraph) - Great utility to draw basic charts (Bar chart, Historgram, heatmap, etc) in the terminal.
 - [kev-dashboard](https://github.com/myseq/kev-dashboard) *[archived]*
 - [kev-catalog](https://github.com/myseq/kev-catalog) *[archived]*
 - [cisa-known-exploited-vulns](https://github.com/myseq/cisa-known-exploited-vulns) *[archived]*


