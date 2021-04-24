import re
import numpy as np
import csv
import matplotlib.pyplot as plt

names=['hRef', 'uAir', 'zz', 'k', 'hMax', 'uWater']

with open('data') as f:
	lines = f.readlines()
lines = ''.join(lines)

for i in names:
	searchString = lines[lines.find(i)+1 : lines[lines.find(i):-1].find(';')+lines.find(i)]
	s = [float(s) for s in re.findall(r'-?\d+\.?\d*', searchString)]
	exec("%s = %f" % (i,s[0]))

z0=zz
z=np.arange(0,hMax,0.001)
uRef=uAir-uWater
u_star=k*uRef/(np.log(hRef/z0+1))
u=u_star*np.log((z+z0)/z0)/k+uWater

plt.plot(u, z)
plt.grid()
plt.savefig('uProfile.png')

# csvOutput
filename = "constant/uProfile.csv"
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(0, len(z)):
        row=[z[i], u[i], 0, 0]
        csvwriter.writerow(row)

# txtOutput
#with open('system/setExprVariables', 'w') as f:
#    f.write('"ustar = ' + str(u_star) + '"\n')
#    f.write('"z0 = ' + str(z0)  +'"\n')
#    f.write('"k = ' + str(k)  +'"\n')
#    f.write('"uWater = ' +str(uWater) + '"\n')
#    f.write('"ustar = ' + str(u_star) + '"\n')
#    f.write('"z0 = ' + str(z0)  +'"\n')
#    f.write('"k = ' + str(k)  +'"\n')
#    f.write('"uWater = ' +str(uWater) + '"\n')
