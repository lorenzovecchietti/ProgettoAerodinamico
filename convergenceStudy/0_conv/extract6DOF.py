sourcefile = 'log.interFoam_9'


fpw = open('6DOF_9.dat', 'w')
line_new = '{:<12}  {:>12}  {:>12}'.format('# Time', 'CM z', 'CM Uz')
fpw.write(line_new + '\n')

fp = open(sourcefile, 'r')
for line in fp:
	if line.startswith('Time = '):
		time = line.rstrip().lstrip('Time = ')
	if line.lstrip().startswith('Centre of mass'):
		CMz = line.split(')')[0].split(' ')[-1]
	if line.lstrip().startswith('Linear velocity'):
		Uz = line.split(')')[0].split(' ')[-1]
		line_new = '{:<12}  {:>12}  {:>12}'.format(time, CMz, Uz)
		fpw.write(line_new + '\n')
		

fp.close()
fpw.close()
