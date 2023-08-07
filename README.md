# breast-cancer-stats

This repository holds source code and examples on how to extract and visualize
breast cancer data from the World Health Organization (WHO) database.

## Setup
A python package without useful utility tools was developed to aid extraction
and visualization. The package is compatible with `Python >= 3.8` and has the
following dependencies:

* pandas

* numpy

* matplotlib

Start by creating a virtual environment and installing the package:

```
virtualenv -ppython3 venv --clear
source venv/bin/activate
python3 -m pip install who_extract@https://github.com/andreped/breast-cancer-stats.git
```

