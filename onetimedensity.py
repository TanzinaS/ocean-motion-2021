from netCDF4 import Dataset 
import matplotlib.pyplot as plt 
import numpy as np 
import seawater as sw
data = Dataset('//Users/brownscholar/desktop/AMNH2021Internship/ocean-motion-2021/intern-data-t0.nc') 
#reading in varible data
temp=data.variables['to'][:] 
sal=data.variables['so'][:] 
depth=data.variables['depth'][:]
s1= sal[0,:,:,:]
t1= temp[0,:,:,:]
d1= depth[0]

den = open('onetimedensity.txt', "w")

den.write("\t"+"\t"+"1"+"\n")
den.write("\t"+"\t"+"158"+"\t"+"\t"+"122"+"\n")

for x in range(0,1):
	for y in range(0, 158):
		for z in range(0, 122):
			density = sw.dens(s1[x,y,z],t1[x,y,z],d1)
			den.write(str(round(float(1000- density), 5)))
			den.write("\t" + "\n")

den.close()

