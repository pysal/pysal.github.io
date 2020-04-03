---
title: "Viz"
icon: "ti-gallery"
description: "Visualize patterns in spatial data to detect clusters, outliers, and hot-spots"
type : "modules"
---

The `viz` layer provides functionality to support the creation of geovisualisations and visual representations of outputs from a variety of spatial analyses. Visualization plays a central role in modern spatial/geographic data science. Current packages provide classification methods for choropleth mapping and a common API for linking PySAL outputs to visualization tool-kits in the Python ecosystem.

### [legendgram](https://github.com/pysal/legendgram)

`legendgram` is a small package that provides "legendgrams" legends that visualize the distribution of observations by color in a given map. These distributional visualizations for map classification schemes assist in analytical cartography and spatial data visualization

### [mapclassify](https://pysal.org/mapclassify)

`mapclassify` provides functionality for Choropleth map classification. Currently, fifteen different classification schemes are available, including a highly-optimized implementation of Fisher-Jenks optimal classification. Each scheme inherits a common structure that ensures computations are scalable and supports applications in streaming contexts.

### [splot](https://splot.readthedocs.io/en/latest/)

`splot` provides statistical visualizations for spatial analysis. It methods for visualizing global and local spatial autocorrelation (through Moran scatterplots and cluster maps), temporal analysis of cluster dynamics (through heatmaps and rose diagrams), and multivariate choropleth mapping (through value-by-alpha maps. A high level API supports the creation of publication-ready visualizations
