# Primero se instala pubchempy con el siguiente comando "pip install pubchempy"
import pubchempy
import pubchempy as pcp

#Ingrese el nombre de el quimico en ingles
chemical_name = input("Ingrese el nombre del elemento quimico en ingles: ")

#Se trae la informacion relacionada a ese nombre de ese quimico 
compound = pcp.get_compounds(chemical_name, 'name')[0]

#Con el siguiente codigo se imprime en pantalla la informacon
print(f"Nombre IUPAC: {compound.iupac_name}")
print(f"Nombre comun: {compound.synonyms[0]}")
print(f"El peso molecular: {compound.molecular_weight}")
print(f"Formula: {compound.molecular_formula}")


    
    










