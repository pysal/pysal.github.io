---
title: "Model"
icon: "ti-panel"
description: "Estimation of spatial relationships in data with a variety of linear, generalized-linear, generalized-additive, and nonlinear models"
type : "modules"
---

In contrast to `explore`, the `model` layer focuses on confirmatory analysis. In particular, its packages focus on the estimation of spatial relationships in data with a variety of linear, generalized-linear, generalized-additive, nonlinear, multi-level, and local regression models.

### [mgwr](https://mgwr.readthedocs.io/en/latest/)

`mgwr` provides scalable algorithms for estimation, inference, and prediction using single- and multi-scale geographically-weighted regression models in a variety of generalized linear model frameworks, as well model diagnostics tools

### [spglm](https://github.com/pysal/spglm)

`spglm` implements a set of generalized linear regression techniques, including Gaussian, Poisson, and Logistic regression, that allow for sparse matrix operations in their computation and estimation to lower memory overhead and decreased computation time.

### [spint](https://github.com/pysal/spint)

`spint` provides a collection of tools to study spatial interaction processes and analyze spatial interaction data. It includes functionality to facilitate the calibration and interpretation of a family of gravity-type spatial interaction models, including those with *production* constraints, *attraction* constraints, or a combination of the two.

### [spreg](https://spreg.readthedocs.io/)

`spreg` supports the estimation of classic and spatial econometric models. Currently it contains methods for estimating standard Ordinary Least Squares (OLS), Two Stage Least Squares (2SLS) and Seemingly Unrelated Regressions (SUR), in addition to various tests of homokestadicity, normality, spatial randomness, and different types of spatial autocorrelation. It also includes a suite of tests for spatial dependence in models with binary dependent variables.

### [spvcm](https://github.com/pysal/spvcm)

`spvcm` provides a general framework for estimating spatially-correlated variance components models. This class of models allows for spatial dependence in the variance components, so that nearby groups may affect one another. It also also provides a general-purpose framework for estimating models using Gibbs sampling in Python, accelerated by the `numba` package.

### [tobler](http://pysal.org/tobler/)

`tobler` provides functionality for for areal interpolation and dasymetric mapping. Its name is an homage to the legendary geographer Waldo Tobler a pioneer of dozens of spatial analytical methods. `tobler` includes functionality for interpolating data using area-weighted approaches, regression model-based approaches that leverage remotely-sensed raster data as auxiliary information, and hybrid approaches.