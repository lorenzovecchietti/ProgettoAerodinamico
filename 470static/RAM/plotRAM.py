import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
from datetime import datetime



fp = open("RAM/logMem.dat", 'r')
for line in fp:
	if line.startswith("RAM:"):
		totRAM = float(line.rstrip().split(":")[1])
	elif line.startswith("SWAP:"):
		totSWAP = float(line.rstrip().split(":")[1])
	else:
		break


hour = []
ram = []
swap = []
for line in fp:
	line = line.strip().split(",")
	if len(line) < 3: continue
	#hrstr = line[0].split(":")
	#hour.append(datetime.time(int(hrstr[0]), int(hrstr[1]), int(hrstr[2])))
	hour.append(line[0])
	ram.append(float(line[1])/totRAM*100)
	swap.append(float(line[2])/totSWAP*100)
fp.close()

hh = [datetime.strptime(i, '%H:%M:%S') for i in hour]
hh = mdates.date2num(hh)
format = mdates.DateFormatter('%H:%M:%S')

figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)

axes.xaxis.set_major_formatter(format)
plt.setp(axes.get_xticklabels(), rotation = 30)
axes.plot(hh, ram, 'r', label='RAM')
axes.plot(hh, swap, 'g', label='Swap')
plt.ylabel("% used")
plt.grid(True, axis="both")
plt.title("Available: RAM = %.2f GB, Swap = %.2f GB" % (totRAM/1024, totSWAP/1024))
plt.legend(loc='best')
#plt.show()
figure.savefig("RAM/RAMUsage.png", dpi=300)
