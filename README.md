# breast-cancer-stats

[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)
<a href="https://colab.research.google.com/gist/andreped/4b0988424c837c8060835ed15b8ee1e9/breast_cancer_mortality_rate_world_map.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

This repository holds source code and examples on how to extract and visualize
breast cancer data from the World Health Organization (WHO) database.

## Setup

A python package without useful utility tools was developed to aid extraction
and visualization. The package is compatible with `Python >= 3.8` and has the
following dependencies:

* numpy

* folium

* pycountry

* geopandas

* Pillow

Note that these dependencies will be installed directly when launching the Jypyter Notebooks.

## Installation

Start by creating a virtual environment and installing the package:

```
virtualenv -ppython3 venv --clear
source venv/bin/activate
python3 -m pip install who_extract@https://github.com/andreped/breast-cancer-stats.git
```

## Usage

Example application notebooks are available in the [apps/](https://github.com/andreped/breast-cancer-stats/apps/) directory.

## Troubleshoot

1) Virtual environment activation

To activate the virtual environment on Windows, instead of `source venv/bin/activate` run `./venv/Scripts/activate`.

2) `ImportError: No module named selenium`

To export the generated map as a PNG image, the [Firefox](https://www.mozilla.org/en-US/firefox/new/) explorer is required.

## License

This repository has [MIT license](https://github.com/andreped/breast-cancer-stats/blob/main/LICENSE).

Note that the CSV files originate from the WHO website (see [here](https://gco.iarc.fr/today/online-analysis-map?v=2020&mode=ranking&mode_population=continents&population=900&populations=900&key=cum_risk&sex=2&cancer=20&type=1&statistic=5&prevalence=0&population_group=0&ages_group%5B%5D=0&ages_group%5B%5D=14&nb_items=10&group_cancer=0&include_nmsc=0&include_nmsc_other=0&projection=natural-earth&color_palette=default&map_scale=quantile&map_nb_colors=5&continent=0&show_ranking=0&rotate=%255B10%252C0%255D)) and have their own respective licences. Hence, if these files are used, you should cite these accordingly.

