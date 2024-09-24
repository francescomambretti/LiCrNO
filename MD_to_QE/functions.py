# Functions to read and write xyz 
# used by Jupyter Notebooks
# N.B.: these functions may be improved with ASE

import numpy as np
import random
import os
import matplotlib.pyplot as plt
import fnmatch
import glob

##################################################################################
def subs_head (natoms):
    s = open("header_scf_template").read().replace("$NATOMS", format(natoms))
    f = open("header_scf", "w")
    f.write(s)
    f.close()
    
    return 

##################################################################################
def read_xyz(filename, skiprows, countermax):
    """Read XYZ file and return atom names and coordinates

    Args:
        filename:  Name of xyz data file

    Returns:
        atom_names: Element symbols of all the atoms
        coords: Cartesian coordinates for every frame.
    """

    print('Reading ',filename)
    coords = []
    count=0
    with open(filename, 'r') as f:
        for _ in range(skiprows):
            next(f)
        if(count< countermax):
            for line in f:
                try:
                    natm = int(line)  # Read number of atoms
                    next(f)     # Skip over comments
                    atom_names = []
                    xyz = []
                    for i in range(natm):
                        line = next(f).split()
                        atom_names.append(line[0])
                        xyz.append(
                            [float(line[1]), float(line[2]), float(line[3])])
                    coords.append(xyz)
                    count+=1
                except (TypeError, IOError, IndexError, StopIteration):
                    raise ValueError('Incorrect XYZ file format')
        else:
            return atom_names, coords 
        
        print('End reading ',filename)

    return atom_names, coords

##################################################################################
def write_xyz(filename, atoms, coords): 
    """Write atom names and coordinate data to XYZ file

    Args:
        filename:   Name of xyz data file
        atoms:      Iterable of atom names
        coords:     Coordinates, must be of shape nimages*natoms*3
    """ 
    natoms = len(atoms)
    with open(filename, 'w') as f:
        for i, X in enumerate(np.atleast_3d(coords)):
            f.write("%d\n" % natoms)
            f.write("Frame %d\n" % i)
            for a, Xa in zip(atoms, X): 
                f.write(" {:3} {:21.12f} {:21.12f} {:21.12f}\n".format(a, *Xa)) 

    return

##################################################################################         
def is_in_range (value, min_int, max_int):
    if value >= min_int and max_int> value:
        return True
    else:
        return False
    
##################################################################################

def histo_force(devi,nbin):

    MF = devi[:,4]
    max_MF = np.amax(MF)
    min_MF = np.amin(MF)
    av_MF = np.average(MF)
    lenMF=len(MF)

    print('Average (eV/A): ', av_MF)
    print('Max (eV/A): ', max_MF)
    print('Min (eV/A): ', min_MF)
    
    plt.clf()

    hist = plt.hist(MF, bins = nbin, color = 'orangered', alpha=0.3)

    # compute max sigma distribution
    sigma_max = hist[1][np.argmax(hist[0])]
    print('Max deviation (eV/A): ', sigma_max)

    plt.vlines(sigma_max, 0, (np.amax(hist[0])+(np.amax(hist[0])*0.1)), color = 'black', linewidth=3)
    plt.title('Histogram of max force deviation')
    plt.xlabel('Max force deviation (eV/A)')
    plt.ylabel('Histogram')
    #plt.xlim(0,0.5)
    plt.rcParams['figure.figsize'] = [3,4]
    plt.show()

    return MF,lenMF

##################################################################################

def sel_conf (MF,lenMF,intervals,N_samples_int,out_path,devi,coords,atoms,t):

    int_geom = [ [] for k in range(3) ] #contains the indexes of the geometries in each interval
    int_Ntot = [0,0,0] # count how many configurations are in each interval
    devi_sel = [] #list of deviations of selected configurations

    for i in range(lenMF): # loop over all configurations
        for j in range(3):
            if MF[i] >= intervals[j][0] and MF[i] < intervals[j][1]:
                int_Ntot[j] += 1
                int_geom[j].append(i)

    for k in range (3):
        print('Configurations interval [{},{}]: {};{}'.format(intervals[k][0],intervals[k][1],int_Ntot[k],int_Ntot[k]/lenMF))

        # Random selection of configurations
        file_geom = out_path+"/run_{}/".format(str(t))+'/geom_int'+str(k)+'.xyz' #set output file names
        selected_geom_int = sorted(random.sample(int_geom[k], N_samples_int[k])) #this contains the sorted indexes of the chosen geometries
        
        for idx in selected_geom_int:
            devi_sel.append(MF[idx]) #keep track of max force deviations of the chosen subset

        #write output 
        print('Writing output resume')
        with open("output.log", 'w') as f:
            f.write("#Selected Frames "+str(k)+" interval:\n")
            f.write("#--------------------------\n")
            for i in range(len(selected_geom_int)):
                f.write("{} {} {} {} {} {} {} {}\n".format(selected_geom_int[i], *devi[selected_geom_int[i]]))
            f.write("#--------------------------\n")

        #write configurations
        selected_coords_int = [coords[i] for i in selected_geom_int]

        print('Writing ',file_geom)
        write_xyz(file_geom, atoms, selected_coords_int)

    #merge files
    os.system("cat "+out_path+"/run_{}/".format(str(t))+"/geom_int*xyz > "+out_path+"/run_{}/".format(str(t))+"/geom_sel.xyz")

    return devi_sel

##################################################################################

def sel_conf_CV (MF,lenMF,intervals,N_samples_int,out_path,devi,coords,atoms,t,cv,min_CV,max_CV):

    int_geom = [ [] for k in range(3) ] #contains the indexes of the geometries in each interval
    int_Ntot = [0,0,0] # count how many configurations are in each interval
    devi_sel = [] #list of deviations of selected configurations
    cv_sel = [] #list of CVs of selected configurations

    for i in range(lenMF): # loop over all configurations
        for j in range(3):
            if MF[i] >= intervals[j][0] and MF[i] < intervals[j][1] and (is_in_range(cv[i],min_CV,max_CV)):
                int_Ntot[j] += 1
                int_geom[j].append(i)

    for k in range (3):
        print('Configurations interval [{},{}]: {};{}'.format(intervals[k][0],intervals[k][1],int_Ntot[k],int_Ntot[k]/lenMF))

        # Random selection of configurations
        file_geom = out_path+"/run_{}/".format(str(t))+'/geom_int'+str(k)+'.xyz' #set output file names
        selected_geom_int = sorted(random.sample(int_geom[k], N_samples_int[k])) #this containst the sorted indexes of the chosen geometries
        
        for idx in selected_geom_int:
            devi_sel.append(MF[idx]) #keep track of max force deviations of the chosen subset
            cv_sel.append(cv[idx])

        #write output 
        print('Writing output resume')
        with open("output.log", 'w') as f:
            f.write("#Selected Frames "+str(k)+" interval:\n")
            f.write("#--------------------------\n")
            for i in range(len(selected_geom_int)):
                f.write("{} {} {} {} {} {} {} {}\n".format(selected_geom_int[i], *devi[selected_geom_int[i]]))
            f.write("#--------------------------\n")

        #write configurations
        selected_coords_int = [coords[i] for i in selected_geom_int]

        print('Writing ',file_geom)
        write_xyz(file_geom, atoms, selected_coords_int)

    #merge files
    os.system("cat "+out_path+"/run_{}/".format(str(t))+"/geom_int*xyz > "+out_path+"/run_{}/".format(str(t))+"/geom_sel.xyz")

    return devi_sel, cv_sel

##################################################################################

def sel_conf_CV_no_int (lenCV,out_path,coords,atoms,t,cv,min_CV,max_CV,Nsamples):

    int_geom = [] #contains the indexes of the geometries in each interval
    cv_sel = [] #list of CVs of selected configurations
    Ntot=0
    
    for i in range(lenCV): # loop over all configurations
        if (is_in_range(cv[i],min_CV,max_CV)):
            Ntot += 1
            int_geom.append(i)
            
    print ('Configurations in the CV interval: [{},{}]: {};{}'.format(min_CV,max_CV,Ntot,Ntot/lenCV))

    file_geom = out_path+"/run_{}/".format(str(t))+'/geom_sel_transition.xyz' #set output file name
    # Random selection of configurations
    if (Nsamples>0):
        selected_geom = sorted(random.sample(int_geom, Nsamples)) #this containst the sorted indexes of the chosen geometries
    else: #take them all
        selected_geom = int_geom
        
    for idx in selected_geom:
        cv_sel.append(cv[idx])

    #write configurations
    selected_coords = [coords[i] for i in selected_geom]

    print('Writing ',file_geom)
    write_xyz(file_geom, atoms, selected_coords)

    return cv_sel


##################################################################################
def sel_conf_flooding(N_samples,out_path,devi,coords,atoms,t):

    file_geom = out_path+"/run_{}/".format(str(t))+'/geom_sel.xyz' #set output file name

    #write configurations
    selected_coords = coords

    print('Writing ',file_geom)
    write_xyz(file_geom, atoms, selected_coords)

    return
    
##################################################################################

def split_xyz(min_id,max_id,out_path,lines_per_split,filename_geom):
    # Loop over replicas  
    for t in range (min_id,max_id+1):
        path = out_path+"/run_{}/".format(str(t))
        myfile=path+filename_geom
        command="split -l "+str(lines_per_split)+" --numeric-suffixes=1 --suffix-length=4 --additional-suffix=\".xyz\" "+myfile+" "+path+"/frame"
        os.system(command)  

    return  

##################################################################################
def create_QE_inp(min_id,max_id,out_path):
    for t in range (min_id,max_id+1):
        path = out_path+"run_{}/".format(str(t))
        try:
            os.makedirs(path+"/inputs_QE")
        except:
            pass
        for a,filename in enumerate(glob.glob(path + '/frame*')):
            os.system("sed -i '1,2d' "+str(filename)+ "&& cat header_scf "+str(filename)+" > "+path+"/inputs_QE/input_"+str(a)+".inp")
    return

##################################################################################
def create_subfold (N,min_id,max_id,out_path):
    groups=0
    old_groups=0
    idx=0
    for t in range (min_id,max_id+1): #  test_list: #range (min_id,max_id+1): #loop over replicas
        path = out_path+"/run_{}/".format(str(t))
        files_per_folder = len(fnmatch.filter(os.listdir(path+"/inputs_QE/"), '*.*'))
        old_groups+=groups
        groups=int(files_per_folder/N)
        print(files_per_folder,groups,old_groups)
        for k in range (0,groups):
            idx=k+(old_groups)
            #print(idx)
            try:
                os.makedirs(path+"/QE_group_"+str(idx))
            except: #folder already exists
                pass 
            for l in range (0,N): #split QE input files across subfolders
                loc_idx=N*k+l 
                try:
                    os.system("cp "+path+"/inputs_QE/input_"+str(loc_idx)+".inp "+path+"/QE_group_"+str(idx))
                except:
                    pass
            #os.system("ls "+main_path+"/QE_group_"+str(idx)+" | wc -l ") - just a check
    return

##################################################################################
def make_tar(min_id,max_id,out_path):
    current_path=os.getcwd() #="/work/fmambretti/uzbeko/MD_to_QE"
    for t in range (min_id,max_id+1): #loop over replicas
        path = out_path+"/run_{}/".format(str(t))
        os.chdir(path)
        os.system("mkdir QE_folders")
        os.system("rm ./QE_folders/*") #in case it exists
        os.system("mv QE_group* QE_folders/")
        os.system("tar -zcvf QE_folders.tar.gz QE_folders/")
        os.system("rm -r QE_folders")
        os.system("rm -r frame*")
        os.system("rm -r inputs_QE")
        os.system("rm *int*")
        os.chdir(current_path)
    return