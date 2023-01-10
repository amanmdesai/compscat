import setuptools

with open('README.md','r') as file:
    long_description = file.read()

setuptools.setup(
name="compscat",
version="0.3.0",
description= "Monte Carlo Simulation of Compton Scattering",
author="Aman Desai",
author_email="amanmukeshdesai@gmail.com",
maintainer="Aman Desai",
maintainer_email="amanmukeshdesai@gmail.com",
url = "https://github.com/amanmdesai/compscat",
long_description=long_description,
packages=["compscat"],
install_requires=["numpy","uproot","matplotlib","pandas"],
long_description_content_type="text/markdown",
classifiers=["License :: OSI Approved :: MIT License",
             "Programming Language :: Python :: 3",
             "Programming Language :: Python :: 3.8",
             "Programming Language :: Python :: 3.9",
             "Programming Language :: Python :: 3.10",
             "Topic :: Scientific/Engineering :: Physics",
             "Operating System :: Unix",
             "Operating System :: Microsoft :: Windows",
             "Operating System :: MacOS"]
)
