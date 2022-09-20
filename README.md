# CompScat
[![License](https://img.shields.io/github/license/amanmdesai/compscat)](https://github.com/amanmdesai/compscat/blob/master/LICENSE.txt)
[![Python package](https://github.com/amanmdesai/compscat/actions/workflows/test.yaml/badge.svg?branch=master)](https://github.com/amanmdesai/compscat/actions/workflows/test.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/amanmdesai/compscat/master.svg)](https://results.pre-commit.ci/latest/github/amanmdesai/compscat/master)
[![Dependency Review](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml/badge.svg)](https://github.com/amanmdesai/compscat/actions/workflows/dependency-review.yml)

[![GH Pages](https://github.com/amanmdesai/compscat/actions/workflows/pages/pages-build-deployment/badge.svg?branch=master)](https://amanmdesai.github.io/compscat/)
[![PyPI Package latest release](https://img.shields.io/pypi/v/compscat.svg)](https://pypi.python.org/pypi/compscat)
[![Supported versions](https://img.shields.io/pypi/pyversions/compscat.svg)](https://pypi.python.org/pypi/compscat)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7096054.svg)](https://doi.org/10.5281/zenodo.7096054)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/amanmdesai/compscat/HEAD)

## Author

Aman Desai

##  Description

Monte Carlo simulation of fixed-target Compton scattering. The study has been compared with Madgraph5amc_NLO MC event generator. The full analysis can be found here [Link](https://github.com/amanmdesai/compscat/tree/master/analysis). The analysis is currently done in C++ (ROOT Framework). To analyse the Madgraph LHE file, an LHE reader deverloped [here](https://github.com/amanmdesai/LHE-Reader) is used.

## Physics

Representative Feynman diagrams for compton scattering
<p align="center">
<img src="analysis/images/compton.png" width="200" title="compton_feyn">
<img src="analysis/images/compton2.png" width="200" title="compton_feyn">
</p>

## Validation of CompScat

The following plots compare the final states for CompScat with the Madgraph5amc_NLO final states.

### Cross section

Evaluated using $10^6$ phase points with CompScat and using the Madgraph file as given in analysis folder.

Plot showing the cross section versus energy (with error bars):
<p align="center">
<img src="analysis/images/xsec_vs_energy.jpg" width="350" title="xsec_vs_energy">
</p>


| Initial Photon Energy | CompScat $\sigma$ (milibarn) | Madgraph $\sigma$ (milibarn)|
| ----------------------| --------- | ------|
|  50 MeV  | 15.585 $\pm$ 0.0495 |  15.57 $\pm$ 0.037  |
| 100 MeV  |  8.783 $\pm$ 0.0361  |  8.799 $\pm$ 0.028   |
| 200 MeV  |  4.857 $\pm$ 0.0255  |  4.87 $\pm$ 0.019    |
| 300 MeV  |  3.414 $\pm$ 0.0205  |  3.43 $\pm$ 0.0081    |
| 400 MeV  |  2.669 $\pm$ 0.0185  |  2.664 $\pm$ 0.0051    |
| 500 MeV  |  2.194 $\pm$ 0.0161  |  2.203 $\pm$ 0.0044   |


### Photon final state kinematics

<p align="center">
<img src="analysis/images/photon_energy.png" width="250" title="photon_energy" />
<img src="analysis/images/photon_px.png" width="250" title="photon_px"/>
</p>

<p align="center">
<img src="analysis/images/photon_py.png" width="250" title="photon_py"/>
<img src="analysis/images/photon_pz.png" width="250" title="photon_pz"/>
</p>

### Electron final state kinematics

<p align="center">
<img src="analysis/images/electron_energy.png" width="250" title="photon_energy">
<img src="analysis/images/electron_px.png" width="250" title="photon_px">
</p>

<p align="center">
<img src="analysis/images/electron_py.png" width="250" title="photon_py">
<img src="analysis/images/electron_pz.png" width="250" title="photon_pz">
</p>

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

## Evaluate the Cross section

See the notebook 'cross-section.ipynb'

## Exercises

* Evaluate the cross section of compton scattering using the `CrossSection` module for different initial proton energies. Plot the same.

* Study the final states at different energies and plot them on the same plot.

* Find the angles $\phi$ and $\theta$ of scattering.

* Make a 2D plot of the energy of photon/electron with the angle of scattering ( $\phi$ and $\theta$).


## Acknowledgements

We would like to thank Dr. Olivier Mattelaer (UCLouvain, Belgium), whose suggestion on applying cuts in the Madgraph configuration file was helpful in validation of the final states predicted by the CompScat package.

## References

1. For physics involved in the calculation, see for example, _Introduction to Elementary Particles_, David Griffiths.
2. For monte carlo techniques: _Statistical data analysis_, Glen Cowan, 1998.
3. For the equations used by the simulator see for example,
[Link](http://www.personal.soton.ac.uk/ab1u06/teaching/qft/qft1/christmas_problems/2014/XmasProb_DMillar.pdf)
4. Also see: Papaefstathiou, A. How-to: write a parton-level Monte Carlo particle physics event generator. Eur. Phys. J. Plus 135, 497 (2020).
5. Alwall, J. and others, The automated computation of tree-level and next-to-leading order differential cross sections, and their matching to parton shower simulations.
