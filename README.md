# CISA KEV

This repo hosts some utilities for CISA KEV.

Previously, those utils are stored separately at [kev-dashboard](https://github.com/myseq/kev-dashboard) and [kev-catalog](https://github.com/myseq/kev-catalog).

> Both repos are in archives mode.

## KEV-Dashboard

This is a simple util that generate a dashboard for CISA's KEV.

This tool is written in python, and it can display the dashboard in two (2) modes: **text mode** or **ASCII chart mode**. 
This tools is created after I got inspirehttps://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csvd by 2 things: 

 - Kenna EPSS distribution per cve/vendor (very cool) and 
 - the command line utility (termgraph) that draws basic graphs in the terminal. 

So I decided to take up the challenge to create a similar tool for both the idea.

## KEV-Catalog

This util show catalog of Known Exploited Vulnerabilities (KEV) from CISA.

This tool is written in Python to shows the top-N vendors and the top-N vulnerable products found in the CISA's KEV. 
It also can search a specific CVE or keyword in the KEV json file.

It includes the function:

 - To save the JSON file from CISA website.
 - Perform local search based on JSON file.

## Links

 - CISA [KEV Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
   - Download the [JSON file](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) directly
   - Download the [CSV file](https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv) directly
 - [Termgraph](https://github.com/mkaz/termgraph) - Great utility to draw basic charts (Bar chart, Historgram, heatmap, etc) in the terminal.

## MySeq Blog

 - <https://myseq.blogspot.com/2022/03/cisa-known-exploited-vuln-catalog.html>
 - <https://myseq.blogspot.com/2022/04/publish-kev-catalog-on-github.html>
 - <https://myseq.blogspot.com/2022/04/kev-dashboard.html>


