#task 1 Surface air temperature
import xarray as xr
ds = xr.open_dataset('/data/pdap/exam2/gistemp250_GHCNv4.nc')
#extract temperature anomaly data from dataset
temps = ds.tempanomaly
#Plot the average surface temperature anomaly
import cartopy.crs as ccrs
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#calculate mean surface temperature anomaly for given period
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

ax.coastlines()
meantemperature=temps.sel(time=slice('2000-01-15','2009-12-15')).mean('time').plot()

#temps.sel(time=slice('2000-01-15','2009-12-15')).mean('time').plot()
ax.gridlines(draw_labels=True)
plt.title('Mean Surface Temperature Anomaly for period 2000-2009',pad=43)

#task 1.2 plot  temperature time-series at specific locations
#temps.sel(lat=-83.0,lon=-169.0).plot(aspect=2, size=3)
ba=['longtitude:31 degree, latitude:41 degree', 
   'longtitude:51 degree, latitude:51 degree',
   'longtitude:111 degree, latitude:51 degree']
a2= temps.sel(lat=41,lon=31).plot()#plot time-series of three different locations
a3= temps.sel(lat=33,lon=51).plot()
a4= temps.sel(lat=51,lon=111).plot()
plt.title('Temperature Anomaly Time Series of three geographical locations')
plt.legend(ba,bbox_to_anchor=[1.8, 1], loc='upper right') #set legend
import os
os.path.abspath('pythonproject2.ipynb')



#task 1.3
from scipy import stats
geodata1=temps.sel(lat=41,lon=31)
geodata2=temps.sel(lat=33,lon=51)
geodata3=temps.sel(lat=51,lon=111)
#calculate annual average
da1 = geodata1.groupby('time.year').mean('time')
da2 = geodata2.groupby('time.year').mean('time')
da3 = geodata3.groupby('time.year').mean('time')
#plot temperature time-seires for three sites
geodata1.groupby('time.year').mean('time').plot()
geodata2.groupby('time.year').mean('time').plot()
geodata3.groupby('time.year').mean('time').plot()
plt.legend(ba)
plt.title('Annual Average temperature anomaly at three geographical sites')
#yearnumber is different since there are some NANs in annual temperature data from site 2 and 3
def temperaturetrend_cal(latitude,longtitude):
    data=temps.sel(lat=latitude,lon=longtitude)
    ydata_annual=np.nan_to_num(data.groupby('time.year').mean('time'))#use nan_to_num to replace all nan data in xarray by zero
    xdata_size=ydata_annual.size#make sure datapoints in x-axis has same dimension as that in y-axis
    xdata =np.linspace(1880,1879+xdata_size,xdata_size)#time data
    m,c,r_value, p_value,std_err= stats.linregress(xdata, ydata_annual)#perform linear regression
    temperaturetrend1=m #slope is temperature trend
    return(temperaturetrend1)
    
print('temperaturetrend1:',temperaturetrend_cal(-25,31),'k/year')


#task 1.4 calculate temperature trend by latitudial dependency and plot their temperature anomaly
latitude_var=['S85-S65', 'S65-S45','S45-S25','S25-S05', 'S05-N15','N15-N35','N35-N55', 'N55-N75']
latitude=[-85,-65,-45,-25,-5,15,35,55,75]
def latitude_temperatureanomaly(longtitude):
    for i in range(8):
        #calculate the annual average temperature anomaly variation per 20 latitude bin
        data=temps.sel(lat=latitude[i+1],lon=longtitude).groupby('time.year').mean('time')-temps.sel(lat=latitude[i],lon=longtitude).groupby('time.year').mean('time')
        data.plot()
        print('temperaturetrend is:',temperaturetrend_cal(latitude[i],longtitude),'k/year for',latitude_var[i])
    plt.legend(latitude_var,bbox_to_anchor=[1.3, 1], loc='upper right')
    

#task 1.5 Analyze the seasonal dependency of temperature changes
seasonal_temperature=temps.resample(time="QS-DEC").mean('time')#calculate seasonal average temperature anomaly
cropdata=seasonal_temperature.sel(time=slice('2000-01-15','2009-12-15'))#limit period to given values
meancropdata=cropdata.groupby('time.season').mean('time')# calculate seasonal mean anomaly
#plot data
meancropdata[0].plot()
plt.title('Winter Mean Temperature Anomaly for Period 2000-2009')
plt.show()
meancropdata[1].plot()
plt.title('summer Mean Temperature Anomaly for Period 2000-2009')
plt.show()
meancropdata[2].plot()
plt.title('Spring Mean Temperature Anomaly for Period 2000-2009')
plt.show()
meancropdata[3].plot()
plt.title('Autumn Mean Temperature Anomaly for Period 2000-2009')



#1.6  Create a map of temperature trends
latitude_coordinate=temps.coords['lat']
newlat=latitude_coordinate.sel(lat=slice(-89, -87))
longtitude_coordinate=temps.coords['lon']
newlon=longtitude_coordinate.sel(lon=slice(-179, -169))
globaltemperaturetrend=[]
#latcor=[]
#loncor=[]
def globalmap():
    for i in  latitude_coordinate:
    
        for j in longtitude_coordinate:
            #latcor.append(i)
           # loncor.append(j)
            if temps.sel(lat=i,lon=j).dropna('time').size>=2:#check if there are sufficient data for linear regression
                Trend=temperaturetrend_cal(i,j)
            else:
        
                Trend=0  #if not, set zero
            
            globaltemperaturetrend.append(Trend)
            if(i==89 and j==179):
                # xr.DataArray(globaltemperaturetrend, coords=[latcor, loncor], dims=['time', 'space'])
                #xr.Dataset(data_vars={ globaltemperaturetrend},
    #coords={'lat': latcor, 'lon': loncor})
                k=np.array(globaltemperaturetrend).size
                l=np.array(latitude_coordinate).size
                m=np.array(longtitude_coordinate).size
                trendafterreshape=np.array(globaltemperaturetrend).reshape(l,m)
                xr.DataArray(trendafterreshape, coords=[np.array(latitude_coordinate),np.array(longtitude_coordinate)],
                                    dims=['lat','lon']).plot()                              
                plt.title('Global Temperature Trend Distribution' )
