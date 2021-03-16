from netCDF4 import Dataset 
import numpy as np 
import seawater as sw
import datetime as dt 

data = Dataset('//Users/brownscholar/desktop/AMNH2021Internship/ocean-motion-2021/intern-data-t0.nc') 
#reading in varible data

time= data.variables["time"]
startdate= dt.datetime(1950,1,1,0,0,0)
for dayindex in range(time.shape[0]):
	currentdate = startdate+dt.timedelta(hours=int(time[dayindex]))
	day= currentdate.strftime("%y")+ currentdate.strftime("%m")+currentdate.strftime("%d")

temp=data.variables['to'][dayindex,:,:,:]
sal=data.variables['so'][dayindex,:,:,:]
depth=data.variables['depth'][:]
#s1= sal[0,:,:,:]
#t1= temp[0,:,:,:]
#d1= depth[0]

file = open("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/Densityfiles/density_"+str(day)+".gr", "w")
file.write("")
file.close()

file = open("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/Densityfiles/density_"+str(day)+".gr", "w")
file.write("\t"+"\t"+"1"+"\n")
file.write("\t"+"\t"+"158"+"\t"+"\t"+"122"+"\n")

for x in range(0,1):
	for y in range(0, 158):
		for z in range(0, 122):
			density = sw.dens(sal[x,y,z],temp[x,y,z],depth[0])
			file.write(str(round(float(1000- density), 5)))
			file.write("\t" + "\n")

file.close()

