# CompScat
[![License](https://img.shields.io/github/license/amanmdesai/compscat)](https://github.com/amanmdesai/compscat/blob/master/LICENSE.txt)
[![gh actions](https://github.com/amanmdesai/compscat/actions/workflows/test.yaml/badge.svg)](https://github.com/amanmdesai/compscat/actions)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/amanmdesai/compscat/master.svg)](https://results.pre-commit.ci/latest/github/amanmdesai/compscat/master)
[![Dependency Review](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Version](https://img.shields.io/github/v/tag/amanmdesai/compscat?style=plastic
)](https://github.com/amanmdesai/compscat/VERSION)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amanmdesai/compscat/HEAD)


##  Description

Monte Carlo simulation of fixed target Compton scattering for educational purposes. The study has been compared with Madgraph5amc_NLO MC event generator and gives the same result for 100 MeV photon colliding with electron at rest for 10k events. The full analysis can be found here [LINK](https://github.com/amanmdesai/compscat/tree/master/analysis). The analysis is currently done in c++ (ROOT Framework). To analyse the Madgraph LHE file, a LHE reader deverloped [here](https://github.com/amanmdesai/LHE-Reader) is used.

## Physics

--- this section explains the physics involved in CompScat ---

## Validation of CompScat

The following plots compare the final states for CompScat with the Madgraph5amc_NLO final states. The comparison is for a 100 MeV photon colliding with electron at rest.

## Installation
```bash
git clone https://github.com/amanmdesai/compscat.git
cd compscat
pip install .
```

## Run the generator!

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
Finally the scripts below will plot the data and store it as pdf. If you have saved the events in a root format use:
```python
compscat.PlotData.file("MC_compton.root")
```
else if you are using csv file, use:
```python
compscat.PlotData.file("MC_compton.csv")
```
## Exercises

* Evaluate the cross section of compton scattering using the `CrossSection` module for different initial proton energies. Plot the same.

* Study the final states at different energies and plot them on the same plot.

* Find the angles $phi$ and $theta$ of scattering.

* Make a 2D plot of the energy of photon/electron with the angle of scattering ($phi$ and $theta$).

## To do

Lorentz Transformation from fixed target frame to center of mass frame. (for the next version.)

## Author
Aman Desai
