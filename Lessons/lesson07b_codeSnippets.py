### Geo Data Science with Python
# Code snippets of lesson 07b
# S. Werth, October, 2021
# ---------------------------------------


# ---- PART I: Point and Polygon examples

# Create Point objects
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)

# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)



# ---- PART II: Import data

import numpy as np
from netCDF4 import Dataset
ncData = Dataset('./tos_O1_2001-2002.nc')

# reading data from netcdf file tos_O1_2001-2002.nc
lat = ncData.variables['lat'][:].data
lon = ncData.variables['lon'][:].data
ncTime = ncData.variables['time'][:].data
ncMask = ncData.variables['tos'][:].mask
tos = ncData.variables['tos'][:].data
tos[tos==1e20] = np.nan
ncData.close()
lonGrid, latGrid = np.meshgrid(lon,lat)


# reading the boundary of the Atlantic from csv file using numpy
filename = "./Atlantic.csv" 
atlanticBnd = np.genfromtxt(filename, delimiter=',', skip_header=1) 

# plotting the 'tos' data for the month of June and the atlanticBnd
import matplotlib.pyplot as plt
plt.pcolormesh(lonGrid,latGrid, tos[5],shading='auto') 
plt.plot(atlanticBnd[:,1], atlanticBnd[:,0], 'k--')
cbar = plt.colorbar()

# adding labels
cbar.set_label('degree Celsius')
plt.title("Sea Surface Temperature, Jun/2001")




# ---- PART III: Data Subset

# setting boundaries of the new data frame for our analysis
# setting boundaries of the new data frame for our analysis
latMin = -10
latMax = 80
lonMin = 260  # lon coordinates in this dataset go from 0...360!!!
lonMax = 360  # lon coordinates in this dataset go from 0...360!!!

# Finding indexes in the datasets that belong to the new boundaries
idx_latMax = np.argmin(np.abs(lat-latMax))
idx_latMin = np.argmin(np.abs(lat-latMin))
idx_lonMax = np.argmin(np.abs(lon-lonMax))
idx_lonMin = np.argmin(np.abs(lon-lonMin))

# reducing the data and coordinate arrays to this frame
# only adjusting coordinate dimensions, not the time dimension (first one)
tos_NW = tos[:,idx_latMin:idx_latMax,idx_lonMin:idx_lonMax]
lon_grid_NW = lonGrid[idx_latMin:idx_latMax,idx_lonMin:idx_lonMax]
lat_grid_NW = latGrid[idx_latMin:idx_latMax,idx_lonMin:idx_lonMax]

# reducing also the 1D coordinate arrays
lon_NW = lon[idx_lonMin:idx_lonMax]
lat_NW = lat[idx_latMin:idx_latMax]





# ---- PART IV: Convert time vector

# importing functions datetime and timedelta from the datetime module
from datetime import datetime
from datetime import timedelta

datetime(2001, 1, 1) + timedelta(15)   # adding 15 days to the date 2001/01/01

# adding number of days in ncTime to the date 2001/01/01
ncTime_date = [ datetime(2001, 1, 1) + timedelta(date) for date in ncTime ]





# ---- PART V: Calculate average tos in 2001 for each grid point in the Atlantic bounding box

# generate new array of same spatial size as the tos dataset 
#   should receive average temperatures during the first year (2001)
average2001_NW = np.zeros(tos_NW.shape[1:])

# nested loop to check if points inside polygon and fill the mask

# iterate through longitude array
for lo_i in range(len(lon_NW)):
    
    # iterate through latitude array
    for la_i in range(len(lat_NW)):
        
        # average over the first 12 records in the time series for current grid points
        # for that we slice out the time series of the current grid point from ncTos_NW:
        curr_timeSeries = tos_NW[:12,la_i,lo_i]
          
        # Then, we have to catch those cases with any nan entries
        # (the nanmean function creates a warning if all entries are nan)
        if (np.any(np.isnan(curr_timeSeries))):
            # assign np.nan to resulting grid point, if nan value in time series
            average2001_NW[la_i,lo_i] = np.nan
        else:
            # assign mean of time series to current grid point
            average2001_NW[la_i,lo_i] = np.nanmean(curr_timeSeries)
            
