
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
from datetime import timedelta
import seawater as sw
import datetime as td

data = Dataset("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/intern-data-t0.nc")

geo = data.variables["zo"][:]

for dateIndex in range(0,216):
	z1 = geo[dateIndex,:,:,:]

	start_date = td.date(1993,1,6)
	weeks_from_start = td.timedelta(weeks =dateIndex)
	date = start_date+weeks_from_start
	filename = date.strftime("%y") + date.strftime("%m") + date.strftime("%d")


	geopotential_file = open("/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/Geopotential/"+"geopotential"+ str(filename)+".txt", "w")
	geopotential_file.write("1"+"\n"+"155"+ "\t"+"122"+"\n")
	for x in range(0,1):
		for y in range(0, 155):
			for z in range(0, 122):
				geopotential = (z1[x,y,z])
				geopotential_file.write("\t"+ str(round(float(geopotential*100),5)))
				geopotential_file.write("\n")

	geopotential_file.close()
