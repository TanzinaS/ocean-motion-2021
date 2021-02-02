from netCDF4 import Dataset 
import matplotlib.pyplot as plt 
import numpy as np 

data = Dataset('/Users/brownscholar/desktop/AMNH2021Internship/ocean-motion-2021/intern-data-t0.nc') 

geo=data.variables['zo'][:] 

z1= geo[0,:,:,:]

print(geo.shape)


geotent = open('geopotential.txt', "w")

geotent.write("\t"+"\t"+"1"+"\n")
geotent.write("\t"+"\t"+"158"+"\t"+"\t"+"122"+"\n")

for x in range(0,1):
	for y in range(0, 158):
		for z in range(0, 122):
			geopot = z1[x,y,z]
			geotent.write(str(round(float(100*geopot), 1)))
			geotent.write("\n")
geotent.close()