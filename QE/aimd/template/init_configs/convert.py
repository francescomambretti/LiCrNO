import ase
from ase.io import read, write
import numpy as np

for j in range (0,3):
    atoms = ase.io.read("conf"+str(j)+".data",style="atomic",format='lammps-data')
    for i,el in enumerate(atoms):
        if el.symbol=="H":
            atoms[i].symbol="Li"
        elif el.symbol=="He":
            atoms[i].symbol="Cr"    

        elif el.symbol=="Li":
            atoms[i].symbol="N"

        elif el.symbol=="Be":
            atoms[i].symbol="O"

        elif el.symbol=="B":
            atoms[i].symbol="H"

        else:
            print("Error")
    write("conf"+str(j)+".xyz",atoms,format="xyz")
