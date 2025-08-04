import numpy as np
import matplotlib.pyplot as plt

def plot_ammonia_conversion(types, temperature, conv_heat, conv_cool):

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(8, 6))

    colors = ['mediumorchid', 'darkcyan', 'yellowgreen']
    labels = ['industrial Ni-based', 'Li$_{14}$Cr$_2$N$_8$O', 'inert filler SiC']
    # loop over ["Ni", "LiCrNO", "SiC"] and plot the data
    for i, type in enumerate(["Ni", "LiCrNO", "SiC"]):
        # Create a mask for the current type
        mask = types == type
        # Plot the data for the current type
        ax.plot(temperature[mask], conv_heat[mask], label=labels[i]+', heating', marker='o',ls="--",color=colors[i])
        ax.plot(temperature[mask], conv_cool[mask], label=labels[i]+', cooling', marker='*',ls="--",color=colors[i])

    #set marker size for all markers
    for line in ax.get_lines():
        line.set_markersize(12)

    # set xticks and yticks with fontsize 16
    ax.set_xticks(np.arange(673, 874, 50))
    ax.set_yticks(np.arange(0, 101, 20))
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.ylim(-5,105)
    plt.xlim(668,878)

    plt.xlabel("Temperature [K]", fontsize=18)
    plt.ylabel("NH$_3$ conversion rate (%)", fontsize=18)
    plt.legend(fontsize=15, loc='upper left')

    plt.savefig("ammonia_conversion_plot.png",dpi=300)

# load data from data.dat and call the function
types,temperature,conv_heat,conv_cool = np.loadtxt("data.dat", dtype=str,unpack=True)

# Convert the data to float where necessary
temperature = temperature.astype(float)
conv_heat = conv_heat.astype(float)
conv_cool = conv_cool.astype(float)
# Call the function to plot the data
plot_ammonia_conversion(types, temperature, conv_heat, conv_cool)

    
