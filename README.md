# CompScat
[![License](https://img.shields.io/github/license/amanmdesai/compscat)](https://github.com/amanmdesai/compscat/blob/master/LICENSE.txt)
[![gh actions](https://github.com/amanmdesai/compscat/actions/workflows/test.yaml/badge.svg)](https://github.com/amanmdesai/compscat/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/amanmdesai/compscat/master.svg)](https://results.pre-commit.ci/latest/github/amanmdesai/compscat/master)
[![Dependency Review](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml)

##  Description

Monte Carlo Simulation of Compton Scattering

## Installation
```bash
git clone https://github.com/amanmdesai/compscat.git
cd compscat
pip install .
```
## Running it!

Description of the example in notebooks:

To import the library use
```python
from compscat import *
```
and then set the energy of the incoming photon in MeV:
```python
E = 0.1
```

The step below is the crucial step as the Cross Section is evaluated here. Only the energy is passed as an argument.
```python
w_sum, w_square, w_max = compscat.CrossSection(
    E / compscat.constants.m
).integrate_xsec()
```
The script below will generate the events according to the w_max obtained above and Energy specified by the user. Moreover, the below class will also save the events (either as root or in a csv file). To save in root format use:
```python
compscat.SaveEvent(10000, w_max, E).to_root()
```
else to save them in a csv file use:
```python
compscat.SaveEvent(10000, w_max, E).to_csv()
```
Finally the scripts below will plot the data and store it as pdf:
```python
compscat.PlotData.file("MC_compton.root")
compscat.PlotData.file("MC_compton.csv")
```

## Author
Aman Desai (https://github.com/amanmdesai)
