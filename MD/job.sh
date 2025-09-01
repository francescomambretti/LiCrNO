#!/bin/bash -l
#PBS -l select=1:ncpus=1:mpiprocs=1:ngpus=1:ompthreads=1
#PBS -l walltime=24:00:00
#PBS -j oe
#PBS -N 10NH-8NH2-1NH3-unb
#PBS -q gpu  

source /projects/atomisticsimulations/Manyi/Miniconda3-DeepMD-2.2.1.env

cd $PBS_O_WORKDIR
lmp -i input.lammps  1>> model_devi.log 2>> model_devi.log 
