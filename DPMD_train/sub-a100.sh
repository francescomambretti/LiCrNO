#!/bin/bash -l
#PBS -l select=1:ncpus=5:mpiprocs=1:ngpus=1:ompthreads=5
#PBS -l walltime=24:00:00
#PBS -j oe
#PBS -q gpu_a100

source /projects/atomisticsimulations/Manyi/Miniconda3-DeepMD-2.2.1.env

cd $PBS_O_WORKDIR

if [ ! -f tag_0_finished ] ;then  #if the file tag_0_finished exists, check the (possible) presence of checkpoints (for restart)
#{ if [ ! -f model.ckpt.index ]; then dp train --skip-neighbor-stat --mpi-log=master input.json; else dp train --mpi-log=master input.json --restart model.ckpt; fi }  1>> train.log 2>> train.log 
  { if [ ! -f model.ckpt.index ]; then dp train --init-frz-model frozen_model14.pb --mpi-log=master input.json; else dp train --mpi-log=master input.json --restart model.ckpt; fi }  1>> train.log 2>> train.log 
  if $? -ne 0; then touch tag_failure_0; fi 
fi

if [ ! -f tag_1_finished ] ;then #training is over, freeze the model
  dp freeze  1>> train.log 2>> train.log 
  touch tag_1_finished 
fi

if [ ! -f tag_2_finished ] ;then #compress the model
  dp compress   1>> train.log 2>> train.log 
  touch tag_2_finished 
fi
