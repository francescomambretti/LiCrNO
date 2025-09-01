import numpy as np
import os
from random import seed
from random import randint

nruns=6
current_folder=os.getcwd()
mother="."
seed(27893)

for c in range(2,2+nruns):
    target_folder=mother+"/run_"+str(c)
    try:
        os.makedirs(target_folder)
    except:
        pass
    s = open("input.lammps").read()
    s = s.replace("$SEED2", format(randint(0,100000)))
    f = open(target_folder+"/input.lammps", "w")
    f.write(s)
    f.close()
    os.system("cp -r job.sh "+target_folder)
    os.system("cp init_configs/conf_10NH_8NH2_1NH3.data "+target_folder+"/conf.data")
    os.chdir(target_folder)
    os.system("qsub job.sh")
    os.chdir(current_folder)

