#!/bin/bash -l
#
#SBATCH --job-name="charge-LiCrNO"
#SBATCH --time=02:00:00
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

echo "start running QE..."

mkdir charges

for name in `ls -v ./input*`
  do
    prefix=${name%.inp}
    srun --cpu-bind=cores pw.x -in ${prefix}.inp > ${prefix}.out
    srun --cpu-bind=cores pp.x -in pp1.inp > charges/${prefix}.out
    srun --cpu-bind=cores pp.x -in pp2.inp > charges/${prefix}.out
    /leonardo/home/userexternal/fmambret/bader density_val.cube -ref density_all.cube
    mv ACF.dat charges/${prefix}.ACF.dat 
    rm -rf ./tmp AVF.dat BCF.dat MO dens*
  done
