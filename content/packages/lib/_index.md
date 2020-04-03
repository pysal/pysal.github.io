---
title: "Lib"
icon: "ti-vector"
description: "Core spatial data structures, file IO. Construction and interactive editing of spatial weights matrices & graphs. Alpha shapes, spatial indices, and spatial-topological relationships"
type : "modules"
---

solve a wide variety of computational geometry problems including graph construction from polygonal lattices, lines, and points, construction and interactive editing of spatial weights matrices & graphs - computation of alpha shapes, spatial indices, and spatial-topological relationships, and reading and writing of sparse graph data, as well as pure python readers of spatial vector data. Unike other PySAL modules, these functions are exposed together as a single package.

### [libpysal](https://pysal.org/libpysal)

`libpysal` provides foundational algorithms and data structures that support the rest of the library. This currently includes the following modules: input/output (`io`), which provides readers and writers for common geospatial file formats; weights (`weights`), which provides the main class to store spatial weights matrices, as well as several utilities to manipulate and operate on them; computational geometry (`cg`), with several algorithms, such as Voronoi tessellations or alpha shapes that efficiently process geometric shapes; and an additional module with example data sets (`examples`).
