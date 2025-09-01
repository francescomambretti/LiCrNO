import os

nruns=10
current_folder=os.getcwd()

for c in range(0,nruns):
    target_folder="328/run_"+str(c)
    try:
        os.makedirs(target_folder)
    except:
        pass
    os.system("tail -n+3 template/init_configs/conf_start.xyz > conf.local") #skip first two lines
    os.system("cat template/md.in conf.local > "+target_folder+"/md.in")
    os.system("cp template/run.sh "+target_folder)
    os.chdir(target_folder)
    os.system("sbatch run.sh")
    os.chdir(current_folder)
os.system("rm conf.local")


