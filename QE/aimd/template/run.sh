#!/bin/bash -l
#
#SBATCH --job-name="aimd-H2"
#SBATCH --time=24:00:00
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:4
#SBATCH --account=IscrB_GRANCOCA
#SBATCH --partition boost_usr_prod
#========================================
# load modules and run simulation
module load profile/chem-phys
module load quantum-espresso/7.2--openmpi--4.1.4--nvhpc--23.1-openblas-cuda-11.8  
export OMP_NUM_THREADS=${SLURM_CPUS_PER_TASK}
export NO_STOP_MESSAGE=1
export CRAY_CUDA_MPS=1
ulimit -s unlimited

srun --cpu-bind=cores pw.x -inp md.in  > OUTPUT.out  
