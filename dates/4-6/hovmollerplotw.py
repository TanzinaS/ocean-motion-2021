import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import datetime as td


original_data = Dataset("/Users/brownscholar/Desktop/atlantic-data.nc")
warray = original_data.variables['w'][:]
lat = 150
latitude=original_data.variables['latitude'][lat]
lon= 118
time= 1355
latlen=156
timeslice = warray[:,lat,:,0].reshape(time,lon)
rotslice = np.rot90(timeslice)

top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')
#x axis
startdate = td.date(1950,1,1)
oritime = original_data.variables['time'][:]

yearlist = []
for i in (range(0,len(oritime),52)):
    yearss = startdate + td.timedelta(hours = int(oritime[i]))
    yearlist.append(yearss.year)


#y axis
longitude_values = original_data.variables['longitude'][:]
for i in range(len(longitude_values)):
    longitude_values[i] = longitude_values[i] - 360


_min = 0
_max = 1355
fig, ax = plt.subplots()
#ax.pcolormesh(rotslice,cmap=newcmp,vmin=_min,vmax=_max)
ax.set_xticks(np.arange(0,1355,52))
ax.set_xticklabels(yearlist,rotation = 90,fontsize=7)
ax.set_yticks(np.arange(0, 118, 20))
ax.set_yticklabels(longitude_values[0::20],fontsize=7)
#now use the following function to plot your data:
#function to make colorplot is:
# p = plt.pcolormesh(V,cmap = newcmp), where V is the numpy array with the data
p = plt.pcolormesh(rotslice,cmap = newcmp, vmax = 1, vmin= -1 )
plt.colorbar(p)
plt.ylabel("Longitude")# labels x axis
plt.xlabel("Years")# labels the y axis
plt.title("Hovmoller diagram at latitude = " + str(latitude) + " degrees N")# labels the entire map
plt.scatter([],[], color = "blue", label = "going down")#lables legend
plt.scatter([],[], color = "red", label = "going up")#lables legend
plt.legend(bbox_to_anchor=[1.0,1.0])# create legend
#plt.xticks(np.arange(0,num_lon,10),lon[::10])
#plt.yticks(np.arange(0,num_lat,10),lat[::10])
plt.show()
