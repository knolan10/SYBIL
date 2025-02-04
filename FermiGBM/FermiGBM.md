# Generating FERMI GBM skymaps corresponding to LIGO skymaps

This directory contains the development work [fermiskymap_testing.ipynb](./fermiskymap_testing.ipynb) and code to generate skymaps for what FERMI GBM would observe given a Kilonovae detected in gravitational waves [fermi_main.py](./fermi_main.py).

## Overview

We start with simulated LIGO NSBH or BNS detections, and use the ra, dec, and luminosity distance. 

We assume a top hat function for gamma-ray burst detectability. We set the probability of detection with the assumption that the jets must be within 15 degrees of the line of sight, although this probabilty can be modified in the script. We set a fixed luminosity at \(2 \times 10^{52} \, \text{ergs/s}\) ([source](https://arxiv.org/pdf/2401.13636)).

Our default detection probability is 60 / 360, assuming two symmetrical jets, either of which can be within 15 degrees of the angle of observation.

If the given event passes this probability cut, we generate a circular GBM skymap with a Gaussian probability distribution, use that distribution to select a location within this GBM skymap for the KN, and translate the GBM skymap so this KN location alligns with the location from the generated LIGO event. To get the radius of the skymap we (1) use the GW luminosity distance and fixed gamma-ray luminosity to get flux and (2) use a fit trend between radius and flux from real gbm data to draw a radius value.

When we simulate GRB detections for a give set of LIGO events, we save a csv file with columns: GW_filename, detected (true/false),GRB_filename,KN_coords. We save each simulated GBM skymap in the format GBM_{nsbh or bns}_{simulated gw id}.npz, which contains numpy arrays of the skymap ras, dec, and probabilities.

## Scientific Assumptions

We do not take into consideration galaxy distributions across the sky when selecting a KN location.

While GBM localizations can be elongated, we currently assume them all to be circular, which appears accurate generally.

We do not take into account GBM sky coverage.

We assume that the jet detectability follows a top hat function, and that jets must be within 15 degrees of the line of sight to be detected.

We randomly generate a gamma-ray burst luminosity which would set the skymap size. This could be modified if there is a correlation between the gravitational wave detection and expected luminosity of the gamma-ray burst.

Improvements: add GBM sky coverage (is 70% so could be significant). The assumption of a fixed luminosity with detection a binary dependent on angle could be made more complex. 

## Dependencies

- `numpy`
- `matplotlib`
- `astropy_healpix`
- `astropy`
- `gdt`

This code was tested with Python 3.12. The not so standard package, gdt (or the Gamma-ray Data Tools), is pip installable with:

```sh
pip install astro-gdt-fermi
gdt-data init

## Example Usage

```sh

python fermi_main.py --LIGO_sim_dir "../skymaps/nsbh1_injection.json" --save_dir "./simulations/nsbh/"