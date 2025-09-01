# LiCrNO
Ammonia decomposition on Li_14_Cr_2_N_8_O, code supporting the paper "Theory Meets Experiment in Ammonia Decomposition on Li_14Cr_2N_8O :From Order to Disorder Under Reaction Conditions", submitted to J. Chem. Phys.

Contents:
- `configs`: intial configurations for ML-MD simulations; bulk, (001) surface, (001) surface with NH and NH_2. There is also a script to cut any surface from the bulk with ASE
- `DPMD_train`: json template input file + scripts to run job (tailored on IIT's Franklin with A100 GPUs)
- `final models`: final trained DPMD models (committee of 4 models). These are the not compressed versions
- `MD`: LAMMPS input file to run biased and unbiased simulations. Plumed example file, and job scripts
- `MD_to_QE`: contains Jupyter Notebooks to select configurations from MD run and re-compute energy and forces on them with Quantum Espresso
- `QE`: contains `aimd` to run ab-initio MD simulations and `scf` for single-point DFT calculations with QE
- `QE_to_DPMD`: bash scripts to correctly change the format of DFT calculations output files to be read by DeepMD for training
