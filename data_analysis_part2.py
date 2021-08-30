#Part 2: Analysis of the Mauna Loa CO2 time series
#Task 2.1
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y')
#names = ['decimal date', 'average', 'interpolated','trend','#day','dd']
a=pd.read_csv('/home/pdap2019/pdap19bj/exams/exam1/exam1_co2-data.txt',engine='python',comment='#',
              delim_whitespace=True,date_parser=dateparse, index_col='1958')

#a.set_index('1958.208')
#a.plot('315.71')
#a.drop(['1958.208'], axis=1, inplace=True)
#measure_time=pd.DataFrame(a[2])
co2_actualvalue=pd.DataFrame(a['315.71'])
co2_actualvalue=co2_actualvalue[co2_actualvalue['315.71']!= -99.99]#deleting missing data dates
#co2_actualvalue1=co2_actualvalue.drop('-99.99')
co2_sketch=co2_actualvalue.plot(grid=True)#plot co2 time series
plt.xlabel('Date of Year')
plt.ylabel('Actual Co2 Value')
plt.legend('Actual Co2 Value')



#Task 2.2
#Create a data frame of the Mauna Loa CO2 measurements, available at ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt, and plot the CO2 time series.  The actual CO2 value is contained in the column average.  Make sure that the index of the DataFrame is actually a DateTimeIndex. 
#The easiest way to achieve this is to use the date_parser kwarg to pd.read_csv().
ka=[ 'Co2 mean','Co2 Minimum','Co2 Maximum']
def sketch_co2data():
    co2mean=co2_actualvalue.groupby(pd.Grouper( freq='Y')).mean().dropna()#calculate the anual mean co2 data
    co2mean=co2mean[co2mean['315.71']!= -99.99]#deleting missing data dates
    co2min=co2_actualvalue.groupby(pd.Grouper( freq='Y')).min().dropna()#calculate the anual min co2 data
    co2min=co2min[co2min['315.71']!= -99.99]#deleting missing data dates
    co2max=co2_actualvalue.groupby(pd.Grouper( freq='Y')).max().dropna()#calculate the anual max co2 data
    co2max=co2max[co2max['315.71']!= -99.99]#deleting missing data dates
    plt.plot( co2mean, 'r') # plotting the anual mean co2 data separately 
    plt.plot( co2min, 'b') # plotting the anual min co2 data separately 
    plt.plot( co2max, 'g') # plotting the anual max co2 data separately 
    plt.xlabel('Date of Year')
    plt.ylabel('Co2 Value')
    plt.legend(ka,bbox_to_anchor=[1.4, 1], loc='upper right')
    
    plt.show()
    
    
#Task 2.3

#load txt file
a=pd.read_csv('/home/pdap2019/pdap19bj/exams/exam1/exam1_co2-data.txt',engine='python',comment='#',
             delim_whitespace=True)   

#Convert.decimal date into formal date as YYYY-MM-DD HH-MM-SS
def is_leap(currentyear):
    if currentyear%4==0:
        return 1
    else:
        return (0)



from datetime import timedelta, datetime

def convert_partial_year(number):

    year = int(number)
    d = timedelta(days=(number - year)*(365 + is_leap(year)))
    day_one = datetime(year,1,1)
    date = d + day_one
    date.strftime("%d %b " )
    return date
#Convert.decimal date into formal date as YYYY-MM-DD HH-MM-SS for all dates
#df2 = pd.DataFrame(a['315.71'])

#a_new=a['1958.208'].astype('float64')
def datetime_create():
   # ma= []#empty array to restore values
    df1 = pd.DataFrame({'date': []})
    #train=pd.DataFrame()
    for i in a['1958.208']:
        i_new=convert_partial_year(i)
        i_new=i_new.strftime("%Y-%m-%d " )
        #i.index=i_new
        df1=df1.append({'date':  i_new},ignore_index=True)
       # a['My new column'] = i_new
        

    if  i==2019.2920000000001:
        return(df1)
    
#function call for formal standard date
datetime_create()

frames = [datetime_create(),a]
alin=pd.concat(frames,axis=1, sort=True,join_axes=[a.index])

datetime_create().reset_index(drop=True, inplace=True)
a.reset_index(drop=True, inplace=True)
alin

#separate data by months
final_transform=alin.set_index('date')#set converted calender date as timeindex
final_transform.index = pd.to_datetime(final_transform.index)
CO2=pd.DataFrame((final_transform['315.71']))
#co2mean1=CO2.groupby(pd.TimeGrouper( freq='M')).mean().dropna()#get monthly averages
CO2.index = pd.to_datetime(CO2.index, format = '%Y-%m-%d').strftime('%m')


#calculate monthly mean Co2 value
month=['01','02','03','04','05','06','07','08','09','10','11','12']
def cal_monthlymean():
    an= pd.DataFrame({'Monthly average Co2 Value':[]})#empty array to restore values 
    
    for j in month:
        a1=CO2.loc[j,'315.71']
        mean=a1.mean()#calculate the means of each month
        an=an.append({'Monthly average Co2 Value':mean},ignore_index=True)
        
    if j=='12':
                return(an)
