import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from sklearn.metrics import mean_absolute_error, mean_squared_error

################# font params

font = {'family' : 'serif',
        'serif'   : 'palatino',
        'style'   : 'normal',
        'variant'   : 'normal',
        'stretch'   : 'normal',
        'weight'   : 'normal'}
plt.rc('font', **font)
offset_cmap=0.2
plt.rcParams['axes.linewidth'] = 2.5

#################
fig, axs = plt.subplots(2, 2, figsize=(8,6))

#plot
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("0_0_0.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
cmap = matplotlib.cm.get_cmap("gnuplot")
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[0,0].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.1),marker='o',linestyle='none')
axs[0,0].set_title("Li$_{14}$Cr$_2$N$_8$O surface",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[0,0].plot(x,x,linestyle='dashed',color='gray')

#load
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("8_8_0.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[0,1].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.3),marker='o',linestyle='none')
axs[0,1].set_title("Li$_{14}$Cr$_2$N$_8$O surface + 8 NH$_3$",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[0,1].plot(x,x,linestyle='dashed',color='gray')

#load
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("16_16_0.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[1,0].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.6),marker='o',linestyle='none')
axs[1,0].set_title("Li$_{14}$Cr$_2$N$_8$O surface + 16 NH$_3$",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[1,0].plot(x,x,linestyle='dashed',color='gray')

#load
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("round15.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[1,1].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.9),marker='o',linestyle='none')
axs[1,1].set_title("N-N bond formation",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[1,1].plot(x,x,linestyle='dashed',color='gray')

'''
#load
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("H-.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[2,0].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.7),marker='o',linestyle='none')
axs[2,0].set_title("H-",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[2,0].plot(x,x,linestyle='dashed',color='gray')

#load
data_x1,data_y1,data_z1,data_x2,data_y2,data_z2=np.loadtxt("H2_aimd.f.out",usecols=(0,1,2,3,4,5),unpack=True)
data_1=np.sqrt(data_x1*data_x1+data_y1*data_y1+data_z1*data_z1)
data_2=np.sqrt(data_x2*data_x2+data_y2*data_y2+data_z2*data_z2)

#plot
mse=np.sqrt(mean_squared_error(data_1, data_2))
axs[2,1].plot(data_1,data_2,label="RMS {:.3f} $eV/\AA$".format(mse),color=cmap(0.9),marker='o',linestyle='none')
axs[2,1].set_title("H$_2$",fontsize=15)
x=np.linspace(0.9*np.min(data_1),1.1*np.max(data_1),1000)
axs[2,1].plot(x,x,linestyle='dashed',color='gray')
'''
for i in range (0,2):
    for j in range (0,2):
        axs[i,j].set_ylabel("|NN force [$eV/\AA$]|",fontsize=14)
        axs[i,j].set_xlabel("|DFT force [$eV/\AA$]|",fontsize=14)
    
        axs[i,j].legend(loc='upper left',fontsize=13,frameon=False)
        axs[i,j].tick_params(axis='both',labelsize=18,direction='in',length=8,width=3,top=True,right=True)

plt.tight_layout()
plt.savefig("NN_vs_DFT.png",dpi=300)
