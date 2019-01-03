---
title: 'Bayesian Integrated and Consilidated (BASIC) composite merging for atmospheric and climate time-series data'
tags:
  - python
  - stratospheric ozone
  - atmospheric time-series
  - time-series analysis
authors:
  - name: Justin A. Alsing
    orcid: 0000-0003-4618-3546
    affiliation: "1, 2, 3"
 - name: Will T. Ball
   orcid: 0000-0002-1005-3670
   affiliation: "4, 5"
affiliations:
 - name: Oskar Klein Center for Cosmoparticle Physics, Stockholm University, Stockholm
   index: 1
 - name: Center for Computational Astrophysics, Flatiron Institute, New York
   index: 2
 - name: Imperial Centre for Inference and Cosmology, Imperial College London, London
   index: 3
 - name: Physikalisch-Meteorologisches Observatorium Davos, World Radiation Center, Davos, Switzerland
   index: 4
 - name: IAC ETH, Zurich, Switzerland
   index: 5
date: 2 January 2019
bibliography: paper.bib
---

# Summary

Constructing atmospheric time-series records spanning multiple decades often involves merging a number of shorter records, from different instruments/observing programs, into a single contiguous composite time-series. Many composites have been published for various atmospheric observables (eg., ozone CITATIONS, water-vapor CITATIONS, etc) and are in common-use for long-term trend analysis, evaluation of chemistry climate models (CCMs), etc. However, composite time-series for the same observables are often discrepant, owing to artefacts that are introduced during the merging process arising from (1) steps in the composite time-series where instrument changes occur, and (1) artificial sub-decadal trends in individual instrument records [@ball2017].

[@ball2017] introduced a Bayesian composite merging algorithm (BASIC) for merging a suite of composite time-series into a single super-merged product that removes many of the artefacts impacting traditional merging techniques, and inflates uncertainties when the data are unable to determine whether (or in which input dataset) artefacts are present. The BASIC approach merges a set of composites into single product in three key steps:

(1) Construct a data-driven estimate of (time-dependent) uncertainties on individual composites using principal component analysis (PCA), and knowledge of when instrument changes occur.
(2) Construct a data-driven seasonal transition prior encoding the statistical distribution of typical eg., month-to-month transitions in the underlying time-series.
(3) Sample the Bayesian posterior of the underlying time-series using the PCA-estimated uncertainties, transition prior, and a Gaussian mixture likelihood to encode the possibility that any individual data point is corrupted by some merging artefact.

The BASIC algorithm is described in detail in [@ball2017]. Here, we provide a public (python) code to generate super-merged BASIC composites, for use by the community. The code takes as input a set of composites to be merged and dates where known instrument changes occured, and returns the artefact-corrected BASIC super-merged product, with associated uncertainties. The python code performs a PCA to estimate uncertainties, constructs the data driven prior, and samples the Bayesian posterior of the underlying time-series using HMC MCMC sampling with stan [@stan].

The BASIC approach applied to stratospheric ozone data has been recommended as a robust choice for long-term trend analysis [@ball2018, @lotus2018] and solar cycle detection (CITE BALL2019 when available).

# References
