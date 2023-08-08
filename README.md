# [breast-cancer-stats](https://github.com/andreped/breast-cancer-stats/edit/main/README.md#breast-cancer-stats)

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
[![DOI](https://zenodo.org/badge/675594864.svg)](https://zenodo.org/badge/latestdoi/675594864)
<a href="https://colab.research.google.com/github/andreped/breast-cancer-stats/blob/main/apps/breast_cancer_incidence_rate.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This repository contains useful notebook examples on how to extract and visualize
breast cancer data from the World Health Organization (WHO) database.

<p style="text-align: left;">
  <img src="assets/incidence.png" width="90%" style="background-color:black">
</p>

## [Dependencies](https://github.com/andreped/breast-cancer-stats/edit/main/README.md#dependencies)

The Notebooks were tested against Python 3.8 on macOS operating system. However, they should be
quite robust against different setups. The following dependencies were used, and are
installed directly through the notebooks:

* [pandas](https://pypi.org/project/pandas/)
* [plotly](https://pypi.org/project/plotly/)
* [nbformat](https://pypi.org/project/nbformat/)
* [kaleido](https://pypi.org/project/kaleido/)

## [Examples](https://github.com/andreped/breast-cancer-stats/edit/main/README.md#Examples)

Example application notebooks are available in the [apps/](https://github.com/andreped/breast-cancer-stats/apps/) directory.

They can be accessed by clicking their respective colab badge below:

| Use case | Notebook |
| - | - |
| Incidence rate world map | <a href="https://colab.research.google.com/github/andreped/breast-cancer-stats/blob/main/apps/breast_cancer_incidence_rate.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| Mortality rate world map | <a href="https://colab.research.google.com/github/andreped/breast-cancer-stats/blob/main/apps/breast_cancer_mortality_rate.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| Overall cancer statistics | <a href="https://colab.research.google.com/github/andreped/breast-cancer-stats/blob/main/apps/breast_cancer_statistics.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |

## [License](https://github.com/andreped/breast-cancer-stats/edit/main/README.md#License)

This repository has [MIT license](https://github.com/andreped/breast-cancer-stats/blob/main/LICENSE).

Note that the CSV files originate from the WHO website (see [here](https://gco.iarc.fr/today/online-analysis-map?v=2020&mode=ranking&mode_population=continents&population=900&populations=900&key=cum_risk&sex=2&cancer=20&type=1&statistic=5&prevalence=0&population_group=0&ages_group%5B%5D=0&ages_group%5B%5D=14&nb_items=10&group_cancer=0&include_nmsc=0&include_nmsc_other=0&projection=natural-earth&color_palette=default&map_scale=quantile&map_nb_colors=5&continent=0&show_ranking=0&rotate=%255B10%252C0%255D)) and have their own respective licences. Hence, if these files are used, you should cite these accordingly.

## [How to cite?](https://github.com/andreped/breast-cancer-stats#How-to-cite)

If you found this project useful, please, consider citing it in your research article:

```
@software{andre_pedersen_2023_8224208,
  author       = {André Pedersen},
  title        = {andreped/breast-cancer-stats: v0.1.0},
  month        = aug,
  year         = 2023,
  publisher    = {Zenodo},
  version      = {v0.1.0},
  doi          = {10.5281/zenodo.8224207},
  url          = {https://doi.org/10.5281/zenodo.8224207}
}
```
