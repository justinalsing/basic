# BASIC

**BAyeSian Integrated and Consilidated (BASIC)** composite super-merging for atmospheric and climate time-series data.

This package implements the BASIC algorithm descibed in [Ball et al 2017](https://www.atmos-chem-phys.net/17/12269/2017/acp-17-12269-2017.html) for constructing a super-merged composite product from a set of potentially artefact biased composite time-series records. 

### Installation

The code is python3 and has the following dependencies (which can be installed using eg., pip install):

[numpy](http://www.numpy.org)<br/>
[pystan](https://pystan.readthedocs.io/en/latest/)<br/>
[scipy](https://www.scipy.org)<br/>

The tutorial `BASIC_tutorial.ipynb` also requires:

[matplotlib](https://matplotlib.org)<br/>
[netCDF4](https://pypi.org/project/netcdf/)<br/>


### Usage

**Functionality**

A detailed annotated tutorial walk-through of how to use the code is given in the jupyter notebook `BASIC_tutorial.ipynb` -- this tutorial builds a BASIC super-merged composite for stratospheric ozone time-series data as an example. The notebook takes you step-by-step through the complete functionality of the code: loading in your own data, running the BASIC merging algorithm, and plotting the results. 

**Pre-built BASIC composite products**

The directory `basic_composites/stratospheric_ozone/` contains a number of pre-built BASIC composite products for stratospheric ozone, that can be downloaded and used out-of-the-box.

The netCDF files include variables for `time`, `pressure` and `latitude` giving the Julian dates* and pressure and latitude grid respectively. The BASIC composite time-series data is given in the variable `o3[time, pressure, latitude]` and associated (time-varying) 1-sigma uncertainties are given in `sigma_o3[time, pressure, latitude]`.

`BASIC_V1_swooshV2.6_gozcardsV1.0_sbuvmodV8.6_sbuvmer.nc` is built from SWOOSH v2.6, GOZCARDS v1.0, SBUV-MOD v8.6 and SBUV-MER (as described in [Tummon et al 2015](https://www.atmos-chem-phys.net/15/3021/2015/)). This corresponds to the BASIC composite presented in [Ball et al 2017](https://www.atmos-chem-phys.net/17/12269/2017/acp-17-12269-2017.html); the data runs up until Dec 2012.

`BASIC_V1_swooshV2.6_gozcardsV2.20.nc` is built from SWOOSH v2.6 and GOZCARDS v2.20; the updated data runs up until Dec 2016. This data was used in [Ball et al 2018](https://www.atmos-chem-phys.net/18/1379/2018/) (referred to as merged-swoosh/gozcards in that paper).


### Citing this code

There is a JOSS paper in preparation to accompany the code (appearing soon), and the method is introduced in detail in [Ball et al 2017](https://www.research-collection.ethz.ch/handle/20.500.11850/202027). Please cite these two papers if you use this code or the resulting BASIC data products.

### Contributions, reporting issues and feature requests

If you want to contribute (eg., extended models) to this package, request a feature, or report a bug/issue, please use the issues channel associated with this Git repository.

