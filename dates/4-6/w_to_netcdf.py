# script to turn w outputs into netcdf
import os
import numpy as np
import datetime
from netCDF4 import Dataset

num_lat = 158
num_lon = 122
levels = 1
dates = 1356
#change to the path to where w file is in (omega-->w)
w_path = '/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/boop/omega/w'#path to w files (created by fortran code)


#change the path to the full data list
date_list = open('/Users/brownscholar/Desktop/AMNH2021Internship/ocean-motion-2021/dates/3-23/date_list-1.txt','r')

w_array = np.zeros((dates,num_lat,num_lon,levels))#creates blank array to fill

for d in range(0,dates):#loops through number of dates
#take out the s_ and if your w file ends in gr its fine, but mine ended in .txt
	filename = (date_list.readline()).strip('\n')+"_ww.txt"#creates file name from date_list
	print(filename)
	if os.path.isfile(w_path+filename):
		w_file = open(w_path+filename,"r")#opens w file
		w_file.readline()#skips the header in w file
		w_file.readline()#skips the header in w file
		for i in range(0,levels):#loops through depth
			for j in range(0,num_lat):#loops through latitude
				for k in range(0,num_lon):#loops through longitude
					w = w_file.readline()
					w_array[d,j,k,i] = float(w)# takes value from w file and puts it into numpy array
					#print(w)


latitude_val = np.arange(12.625+.5,51.875-0.25,0.25)#creates numpy array with all of the latitude values
longitude_val = np.arange(311.875+.5,342.125-0.25,0.25)
time_val = np.arange(377064,604704+168,168)
print(time_val.size)
#change to desktop
#change path to some where you want the nc file to be
grp = Dataset('/Users/brownscholar/Desktop/atlantic_data_1993-2018.nc','w', format='NETCDF4')# opens netcdf file
#creates dimensions in netcdf file
grp.createDimension('lon', num_lon-4)
grp.createDimension('lat', num_lat-4)
grp.createDimension('depth', levels)
grp.createDimension('time', dates)
#creates variables in numpy array
longitude = grp.createVariable('longitude', 'f4', 'lon')#f4 means that the values will be floats
latitude = grp.createVariable('latitude', 'f4', 'lat')#f4 means that the values will be floats
depth = grp.createVariable('depth', 'f4', 'depth')
time = grp.createVariable('time','f4', 'time')
w = grp.createVariable('w', 'f4', ('time', 'lat', 'lon', 'depth'))
#fills the variables in the netcdf file with the values from the numpy arrays
longitude[:] = longitude_val
latitude[:] = latitude_val
time[:] = time_val
depth[:]= [1]

w[:] = w_array[:,2:156,2:120,:]

time.units = 'hours since 1950-01-01'#adds units to netcdf variables
latitude.units = 'degrees_north'#adds units to netcdf variables
depth.units = 'm'#adds units to netcdf variables
depth.positive ='down'
depth.axis = 'Z'

w.units = 'm/day'#adds units to netcdf variables

grp.close()
