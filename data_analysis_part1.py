# python datat analysis project 1
# Data analysis to the ozone measurements 

#Task 0.1
import numpy as np
import pandas as pd
import os
#extract data path
os.path.abspath("20180202.brewer-mast.na.na.dwd-mohp.csv")
os.path.abspath('pythonproject1.ipynb')



#Task1.1
#create dataframe for ozone data for given physical quantities pressure temperature and ozone partial pressure
ozone_data=pd.read_csv('/home/pdap2019/pdap19bj/exams/exam1/20180214.brewer-mast.na.na.dwd-mohp.csv',skiprows=36,engine='python')
ozone_data.head(620)
ozone_data[['Pressure','Temperature','O3PartialPressure']]



#Task 1.2
#plot the diagram of pressure versus temperature
%matplotlib inline
import matplotlib.pyplot as plt
#plt.plot(ozone_data['Temperature'])
df=pd.DataFrame(ozone_data[['Pressure','Temperature']],columns=['A','B'])
df['B']=ozone_data['Temperature']
df['A']=ozone_data['Pressure']
df.plot(x='B',y='A')#plot the result
plt.xlabel('Temperature')
plt.ylabel('Pressure')


#Task 1.3 Calculating the ozone mixing ratio
df=pd.DataFrame(ozone_data[['Pressure','Temperature','O3PartialPressure']])
Ozone_PartialPressure=ozone_data['O3PartialPressure']/1000 #convert mili-pascal into Pascal
Air_pressure=ozone_data['Pressure']*100  #convert hPa into Pascal
mixing_ratio=Ozone_PartialPressure/Air_pressure
plt.plot(mixing_ratio)
plt.xlabel('Pressure')
plt.ylabel('mixing ratio')
df=pd.DataFrame(ozone_data[['Pressure','Temperature','O3PartialPressure']])
df.insert(3, "mixing ratio",mixing_ratio, True)


#Task 1.4 Calculate statistics for one sonde flight
def calc_o3_statistics(filename):
    file=pd.read_csv(filename,skiprows=36,engine='python')
    Ozone_PartialPressure=file['O3PartialPressure']/1000 #convert mili-pascal into Pascal
    Air_pressure=file['Pressure']*100  #convert hPa into Pascal
    mixing_ratio=Ozone_PartialPressure/Air_pressure
    df=pd.DataFrame(file[['Pressure','Temperature','O3PartialPressure']])
    df.insert(3, "mixing ratio",mixing_ratio, True)
    

    mean=mixing_ratio.mean()
    max=mixing_ratio.max()
    min=mixing_ratio.min()

    
    #b=df.Pressure[df['mixing ratio'] == max]
    b=df.Pressure.loc[df['mixing ratio'] == max]
    
   
    return ( 'The mean mixing ratio:',mean, 'the max mixing ratio:',max,'the minimum mixing ratio:',min,'the air pressure at highest mixing ratio:',b) 




#Task 1.5: Calculate statistics for all sonde flights
import glob 

filepath=glob.glob('/home/pdap2019/pdap19bj/exams/exam1/2018*.csv')
a=sorted(filepath)



def calc_statistics(filenumber):
  
    ma= []#empty array to restore values 
    airpressure=[]#empty array to restore values
    for i in a:
        
        sonderflight_values=calc_o3_statistics(i)
        
        maximum=sonderflight_values[3]# find the maximum of each datafile
        airpressure.append(sonderflight_values[7])#restore the air pressure in a list intermediately
        ma.append(maximum)#restore the maximum in a list intermediately
        
        current_filenumber=a.index(i)+1
        #print (maximum)
        if  current_filenumber ==filenumber:
            print (ma)#print maximum mixing ratio
            print(airpressure)#print airpressure
            break  
            
#Task 1.6 Plot statistics for all sonde flights
#  convert a list to string     
# Function to convert  
from datetime import datetime
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1         
     
#get time labels
ba= []#empty array to restore values 
for i in range (12):
    
    date_string = a[i]
    b=listToString(date_string)#convert list to string
    date_time = datetime.strptime(b,"/home/pdap2019/pdap19bj/exams/exam1/%Y%m%d.brewer-mast.na.na.dwd-mohp.csv")
    
   # print(date_time )
    finaltime=date_time.strftime("%d %b " )
    ba.append(finaltime)

    
    
%matplotlib inline

import matplotlib.pyplot as plt    
import datetime
from datetime import date   
def sketch_maximum_o3mixing_ratio():
    #y= pd.DataFrame(calc_statistics(3))    
        xdata=np.linspace(0,12,12) 
        ydata=[7.526555386949924e-06, 7.011406844106465e-06, 6.19774011299435e-06, 9.473684210526315e-06,
               6.646928201332347e-06, 5.621219171707771e-06, 6.741682974559686e-06,8.289322617680825e-06,
               6.523400191021967e-06, 7.347130761994355e-06, 6.648480124707716e-06, 5.722423614707406e-06]#get corresponding maximum mixing ratio from previous function
        plt.ylabel('maximum mixing ratio')
        plt.title('maximum mixing ratio vs Sonder Flight')
        text=plt.plot(xdata,ydata,'r')
        plt.xticks(xdata, ba)
        plt.xticks(rotation=90)
        plt.show()
     
       
   # for i in alist: 
        #String=datetime.datetime.strptime(i,"%d")



def sketch_airpressure():
    #y= pd.DataFrame(calc_statistics(3))    
        xdata=np.linspace(0,12,12)
        #ind = np.arange(12)
        ydata=[580 ,549,500,541,530 ,506, 554 , 579,545, 565 ,525 ,496]
         
        plt.ylabel('air pressure')
        plt.title('air pressure vs Sonder Flight')
        text=plt.plot(xdata,ydata,'b')
        
        plt.xticks(xdata, ba)
        plt.xticks(rotation=90)
        plt.show()
    
    
def sketch_both():
    
    fig, ax1 = plt.subplots()
    x=np.linspace(0,12,12)
    ydata1=[580 ,549,500,541,530 ,506, 554 , 579,545, 565 ,525 ,496]
    ydata2=[7.526555386949924e-06, 7.011406844106465e-06, 6.19774011299435e-06, 9.473684210526315e-06,
               6.646928201332347e-06, 5.621219171707771e-06, 6.741682974559686e-06,8.289322617680825e-06,
               6.523400191021967e-06, 7.347130761994355e-06, 6.648480124707716e-06, 5.722423614707406e-06]
    #plot air pressure
    color = 'tab:blue'
    plt.xticks(x, ba)
    plt.xticks(rotation=90)
    ax1.plot(x,ydata1,color)
    ax1.set_ylabel('air pressure', color=color)
    ax1.tick_params(axis='y', labelcolor=color)#set y1-axis color 
    
    #plot maximum mixing ratio
    ax2 = ax1.twinx()  # set up a second axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('maximum mixing ratio', color=color)
    ax2.plot(x,ydata2,'r')
    ax2.tick_params(axis='y', labelcolor=color)#set y2-axis color
    plt.title('Maximum mixing ratio & Air pressure')
    plt.xticks(x, ba)#set x labels as monthly calender date
    plt.xticks(rotation=90)
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
