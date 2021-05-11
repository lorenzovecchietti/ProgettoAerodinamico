import numpy as np
import os
import csv

############
### Dati ###
############
nPx=5
nPy=5
nPz=5


# Informazioni da paraview: fare box 1x1x1 e usare trasformazione
dx=1
dy=0.3
dz=0.49

finalCenter=np.array([-2.05, -0.11, -0.5])
rotationX=-15

###############
### Calcolo ###
###############
a=np.linspace(0, 1, nPx)*dx-dx/2
b=np.linspace(0, 1, nPy)*dy-dy/2
c=np.linspace(0, 1, nPz)*dz-dz/2

r=np.deg2rad(rotationX)
R=np.array([[1, 0, 0], [0, np.cos(r), -np.sin(r)], [0, np.sin(r), np.cos(r)]])

listPoints=[]
for i in a:
	for j in b:
		for k in c:
			listPoints.append(np.array([i, j, k]))

listPointsRotated=[]
for i in listPoints:
	e=R.dot(i)
	listPointsRotated.append(e+finalCenter)

#########################
### Esportazione File ###
#########################
path="constant/controlPoints/"
os.mkdir(path)

with open(path+'boxcpsBsplines0', mode='w') as pointFile:
        pointFile.write("/*--------------------------------*- C++ -*----------------------------------*\ \n")
        pointFile.write("| =========                 |                                                 | \n")
        pointFile.write("| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           | \n")
        pointFile.write("|  \\    /   O peration     | Version:  v2012                                 | \n")
        pointFile.write("|   \\  /    A nd           | Website:  www.openfoam.com                      | \n")
        pointFile.write("|    \\/     M anipulation  |                                                 | \n")
        pointFile.write("\*---------------------------------------------------------------------------*/ \n")
        pointFile.write("FoamFile \n")
        pointFile.write("{ \n")
        pointFile.write("    version     2.0; \n")
        pointFile.write("    format      ascii; \n")
        pointFile.write("    class       dictionary; \n")
        pointFile.write('    location    "../constant/controlPoints"; \n')
        pointFile.write("    object      boxcpsBsplines0; \n")
        pointFile.write("} \n")
        pointFile.write("// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * // \n")
        pointFile.write("controlPoints   " + str(len(listPointsRotated)) + "( \n")
        for i in listPointsRotated:
              pointFile.write("( " + str(i[0]) + " " + str(i[1]) + " "  + str(i[2])  + ") \n")
        pointFile.write("); \n")
        pointFile.write("// ************************************************************************* //")
