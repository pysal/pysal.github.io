---
title: "Explore"
icon: "ti-map"
description: "Modules to conduct exploratory analysis of spatial and spatio-temporal data"
type : "modules"
image: ""
---

The `explore` layer includes modules to conduct exploratory analysis of spatial and spatio-temporal data. At a high level, packages in `explore` are focused on enabling the user to better understand patterns in the data and suggest new interesting questions rather than answer existing ones. They include methods to characterize the structure of spatial distributions (either on networks, in continuous space, or on polygonal lattices). In addition, this domain offers methods to examine the *dynamics* of these distributions, such as how their composition or spatial extent changes over time.

### [esda](https://esda.readthedocs.io/en/latest/)
`esda` implements methods for the analysis of both global (map-wide) and local (focal) spatial autocorrelation, for both continuous and binary data. In addition, the package increasingly offers cutting-edge statistics about boundary strength and measures of aggregation error in statistical analyses

### [giddy](https://giddy.readthedocs.io/en/latest/)
`giddy` is an extension of `esda` to spatio-temporal data. The package hosts state-of-the-art methods that explicitly consider the role of space in the dynamics of distributions over time

### [inequality](https://inequality.readthedocs.io/en/latest/)
`inequality` provides indices for measuring inequality over space and time. These comprise classic measures such as the Theil *T* information index and the Gini index in mean deviation form; but also spatially-explicit measures that incorporate the location and spatial configuration of observations in the calculation of inequality measures.

### [pointpats](https://pointpats.readthedocs.io/en/latest/)
`pointpats` supports the statistical analysis of point data, including methods to characterize the spatial structure of an observed point pattern: a collection of locations where some phenomena of interest have been recorded. This includes measures of centrography which provide overall geometric summaries of the point pattern, including central tendency, dispersion, intensity, and extent.

### [segregation](https://github.com/pysal/segregation)
`segregation` package calculates over 40 different segregation indices and provides a suite of additional features for measurement, visualization, and hypothesis testing that together represent the state-of-the-art in quantitative segregation analysis.

### [spaghetti](https://pysal.org/spaghetti)
`spaghetti` supports the the spatial analysis of graphs, networks, topology, and inference. It includes functionality for the statistical testing of clusters on networks, a robust all-to-all Dijkstra shortest path algorithm with multiprocessing functionality, and high-performance geometric and spatial computations using `geopandas` that are necessary for high-resolution interpolation along networks, and the ability to connect near-network observations onto the network
