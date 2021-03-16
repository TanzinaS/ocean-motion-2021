from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from datetime import timedelta
import seawater as sw
import datetime as td

data = Dataset("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/intern-data-t0.nc")
#step 1: read in ncdcf file

s = data.variables["so"][:]
t = data.variables["to"][:] #52
d = data.variables["depth"][:] #1
#read in salinity, temperature, depth

for dateIndex in range(0,216):
	s1 = s[dateIndex,:,:,:]
	t1 = t[dateIndex,:,:,:]
	depth = d[0]

	start_date = td.date(1993,1,6)
	weeks_from_start = td.timedelta(weeks =dateIndex)
	date = start_date+weeks_from_start
	filename = date.strftime("%y") + date.strftime("%m") + date.strftime("%d")

	density_file = open("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/Densityfiles/" + "density"+ str(filename)+".txt", "w")
	density_file.write("1"+"\n"+"155"+ "\t"+"122"+"\n")#error??

	for x in range(0,1):
		for y in range(0, 155):
			for z in range(0, 122):
				density = sw.dens(s1[x,y,z],t1[x,y,z],depth)
				density_file.write("\t"+str(round(float(1000-density),5)))
				density_file.write("\n")

#loop through and calculate the densities at each grid point

	density_file.close()
#read the file
#density_file = open("density_file.txt", "r")

"/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/n-atlantic-2018.nc"

#mport and create variable for each type of data
#use nested forloops to make these variables into indices
#run each inxed through the function sw
