Use these Jupyter Notebooks to extract configurations from LAMMPS + DeepMD trajectories and give them to Quantum Espresso.

The `conf_selection*` notebooks are to be used in different situations:
- `conf_selection.3int`: if you want to select configurations based on three intervals along the axis of the Maximum Force Deviation, i.e. based on the deviation among the DeepMD models used
- `conf_selection.3int+CV`: the same as the previous one, together with a chosen range of a collective variable (CV). This has to be used in presence of a COLVAR file, i.e. in case of a simulation run with PLUMED/PLUMED driver
- `conf_selection.CV-no-int`: use just a CV range without considering the model deviations.
- `conf_selection.flooding`: to be used for OPES Flooding simulations. In this case, select just the last `Nsamples` configurations, regardless of their MF deviation.

The `functions.py` file contains all the relevant functions used in the notebooks.

`header_scf_template` is a Quantum Espresso template input file for calculation of atomic forces and energies, to be completed with coordinates (the notebooks merge the template with the current atomistic configurations, creating proper QE input files)
