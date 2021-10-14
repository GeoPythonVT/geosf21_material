"""
Created on Mon Oct 12 18:54:30 2021
@author: swerth
"""
import matplotlib.pyplot as plt
import numpy as np
import netCDF4
from netCDF4 import Dataset
from netCDF4 import date2index
from datetime import datetime


# read netcdf file
data = Dataset('gistemp250_GHCNv4.nc')

# Get index for a certain month
year = 2021
month = 1
timeindex = date2index(datetime(year, month, 15),
                       data.variables['time'])




# read data 
# --------
###  complete the code here
###  read lat, lon, time and anomaly into numpy arrays

###  replace fill values





# plot data 
# --------

# converting the 1D coordinate arrays to a meshgrid
lonGrid, latGrid = np.meshgrid(lon,lat)

# plot data into map
fig = plt.figure(figsize=(10, 6))

# plotting the first last map in the time series
plt.pcolormesh(lonGrid,latGrid, anom, shading='auto') 

# adding a colorbar and title
plt.title('Temperature Anomaly ' + str(datetime(year, month, 15)))
plt.colorbar(label=('temperature anomaly (' + u'\N{DEGREE SIGN}' + 'C)'))

# add plot limits
#plt.clim(-8, 8)


# get available time period in netcdf file and write to screen
t_units = data.variables['time'].units
time_beg = netCDF4.num2date(data.variables['time'][0],t_units)
time_end = netCDF4.num2date(data.variables['time'][-1],t_units)
print('\nThis netcdf file contains records from ' + str(time_beg) +
      ' to ' + str(time_end))