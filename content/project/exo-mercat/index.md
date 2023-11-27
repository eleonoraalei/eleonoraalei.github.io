---
title: Exo-MerCat
summary: The Exoplanet Merged Catalog merges data from the major exoplanet catalog to identify the most precise measurements for the currently known exoplanets (or candidates).
tags:
  - catalogs
  - software


# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: Photo by rawpixel on Unsplash
  focal_point: Smart

links:
#  - icon: twitter
#    icon_pack: fab
#    name: Follow
#    url: https://twitter.com/georgecushen
url_code: 'https://.github.com'
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

The search for exoplanets (i.e. planets that orbit other stars in our Galaxy other than the Sun) has been growing as a bold branch of astrophysics for the past two decades, with more than 5000 confirmed exoplanets known to date. Surveys and missions reveal day by day new candidates and provide us insight concerning their orbital and bulk parameters, and the properties of their host stars. We are now aware of the fact that exoplanets differ from one another in many of these physical parameters, and in the future we should be able to fully understand the diversity of their chemical compositions, atmospheric processes, internal structures and formation conditions.


During my Ph.D., I wrote a Python script that compiles the Exoplanet Merged Catalog (Exo-MerCat). a Python code that collects and selects the most precise measurement for all interesting planetary and orbital parameters of all Super Earths included in the three major exoplanets online databases: NASA Exoplanet Archive, Exoplanet Orbit Database, and Exoplanet Encyclopaedia. By downloading all source files from the three catalogs using VO ConeSearch connections and considering user preferences through a Graphic User Interface, it creates a merged catalog and generates automatically all standard plots.