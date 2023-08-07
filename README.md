# breast-cancer-stats

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

