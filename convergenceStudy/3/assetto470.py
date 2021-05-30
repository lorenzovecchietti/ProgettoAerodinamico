import os
import numpy as np


# ========================================
print("\nSistema di riferimento barca: x indietro, z in alto\n")
roll = input("Angolo di rollio [deg]: ");
yaw  = input("Angolo di imbardata [deg]: ");

os.chdir("constant/triSurface")

cmd = "surfaceTransformPoints -rollPitchYaw '("+str(roll)+" 0 0)' hull470orig.stl hull470.stl"
os.system(cmd)
cmd = "surfaceTransformPoints -rollPitchYaw '(0 0 "+str(yaw)+")' hull470.stl hull470.stl"
os.system(cmd)


os.chdir("../..")
