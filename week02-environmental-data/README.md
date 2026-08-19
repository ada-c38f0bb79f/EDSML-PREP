# Week 2: Environmental Data with Xarray and NetCDF

## Deliverable

- Complete `environmental_data_analysis.ipynb` using a real climate or
  environmental dataset.
- Write `technical_summary.md` (target: approximately 500 words).
- Document the dataset, units, coordinate conventions, missing values, and
  limitations.

## Checklist

- [ ] Explain `DataArray`, `Dataset`, dimensions, coordinates, and attributes.
- [ ] Open or create a NetCDF dataset with Xarray.
- [ ] Select data by labels and coordinates with `.sel()`.
- [ ] Compute at least one temporal or spatial aggregation.
- [ ] Handle missing values and verify units.
- [ ] Produce at least two labelled plots, including one spatial plot if the
      dataset has latitude and longitude.
- [ ] Save a reproducible processed result.
- [ ] Complete the technical summary.

## Official resources and format

- Project Pythia Foundations (18 notebooks; Apache-2.0):
  https://github.com/ProjectPythia/pythia-foundations
- Xarray tutorial (56 notebooks; Apache-2.0):
  https://github.com/xarray-contrib/xarray-tutorial
- Xarray source and documentation (includes NetCDF examples):
  https://github.com/pydata/xarray
- Climatematch climate course (hundreds of project notebooks; BSD-3-Clause):
  https://github.com/ClimateMatchAcademy/climate-course-content
- xCDAT climate-analysis extension (Python package and docs):
  https://github.com/xCDAT/xcdat
- GeoCAT plotting examples (Python scripts/gallery; Apache-2.0):
  https://github.com/NCAR/geocat-examples

Start with the Pythia `xarray-intro.ipynb` and `netcdf-cf.ipynb`, then use the
local notebook for the assessed deliverable.
