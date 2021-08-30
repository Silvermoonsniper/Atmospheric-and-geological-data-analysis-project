#task 2.1 Evaluating a predator-prey (i.e., Lotka-Volterra) system
import numpy as np
from scipy.integrate import odeint
x_intial = [3/4, 0.5]#intial value for number of prey and predator
times = np.linspace(0., 15., 101)
p1,p2,p3,p4 = [2/3,1/3, 1,1/4]
def deriv(cvec, times, alpha, beta,gamma,delta):
    x1,x2 = cvec
    return [alpha* x1-beta*x1*x2, -gamma*x2+delta*x1*x2 ]


solution = odeint(deriv, x_intial, times, args=(p1,p2,p3,p4))

plt.plot(times, solution[:, 0], label='populations change of prey(rabbit)')
plt.plot(times, solution[:, 1], label='populations change of predator(fox)')
plt.xlabel('Population of Rabbit ')
plt.ylabel('Population of Fox ')
plt.legend(bbox_to_anchor=[1.7, 1], loc='upper right')
plt.title('populations variation of prey(rabbit) versus predator(fox)')



#Task 2.2  Investigate the effect of different initial conditions
label=['X1:6 X2:3 time:1-16','X1:9 X2:4 time:1-16','X1:12 X2:6 time:1-16',
       'X1:15 X2:8 time:1-16','X1:18 X2:9 time:1-16']
def integrate_predator_prey(x1_intial, x2_intial, times):
    x_intial = [x1_intial, x2_intial]#intial value for number of prey and predator
    times = np.linspace(times, times+15, 101)
    p1,p2,p3,p4 = [2/3,1/3, 1,1/4]
    solution = odeint(deriv, x_intial, times, args=(p1,p2,p3,p4))
   
    plt.plot(solution[:, 0],solution[:, 1])
    #plt.plot()
    plt.xlabel('Population of Rabbit ')
    plt.ylabel('Population of Fox ')
    plt.title('Population variation of rabbits and foxes at different initial conditions and time slots')
    plt.legend(label,bbox_to_anchor=[1.5, 1], loc='upper right')
    return(solution)
#integrate_predator_prey()
def Graphsketch():
    intialconditionset1=[6,9, 12, 15, 18]
    intialconditionset2=[ 3,  4,  6, 8, 9]
    timelist=[1,2,3,4,5]
#labellist=[]
    for i in range(5):
        for j in range(5):
        #calculate x1 and x2 for allintial conditions at given times
            odesov=integrate_predator_prey(intialconditionset1[j],intialconditionset2[j],timelist[i])
            labellist=[intialconditionset1[j],intialconditionset2[j],timelist[i]]
        
Graphsketch()



#Task 2.3 Draw the direction fields
import scipy
from scipy.misc import derivative
alpha,beta,gamma,delta = [2/3,1/3, 1,1/4]
def integrate_predator_prey_direction(x1_intial, x2_intial, times):
    x_intial = [x1_intial, x2_intial]#intial value for number of prey and predator
    times = np.linspace(times, times+15, 101)
    p1,p2,p3,p4 = [2/3,1/3, 1,1/4]
    solution = odeint(deriv, x_intial, times, args=(p1,p2,p3,p4))
    function=alpha* x1-beta*x1*x2
    x_1=solution[:, 0]
    x_2=solution[:, 1]
    x1_gradient=alpha* x_1-beta*x_1*x_2
    x2_gradient=1
    x1_gradient1=-gamma*x_2+delta*x_1*x_2
    x2_gradient1=1
#gradient=scipy.misc.derivative(solution[:, 0], 1.0, dx=1e-6)   
    plt.plot( solution[:, 0],solution[:, 1])
    #plt.plot(times, )
    plt.xlabel('Population of Rabbit ')
    plt.ylabel('Population of Fox ')
    plt.title('Population variation of rabbits and foxes at different initial conditions and time slots with directional derivatives')
    plt.legend(label,bbox_to_anchor=[1.5, 1], loc='upper right')
    plt.quiver(solution[:, 0],solution[:, 1],x1_gradient,x1_gradient1)
    #plt.quiver(times,solution[:, 1],x2_gradient1,x1_gradient1)
    return(solution)

intialconditionset1=[6,9, 12, 15, 18]
intialconditionset2=[ 3,  4,  6, 8, 9]
timelist=[1,2,3,4,5]
#labellist=[]
#for i in range(5):
for j in range(5):
        #calculate x1 and x2 for allintial conditions at given times
        odesov=integrate_predator_prey_direction(intialconditionset1[j],intialconditionset2[j],timelist[0])
        labellist=[intialconditionset1[j],intialconditionset2[j],timelist[i]]
        
        
#Task 3: Interpolation
#Task 3.1: Preparation
import math
from scipy.interpolate import interp1d
xdata=np.linspace(-math.pi,math.pi,101)
xdatacos=np.cos(xdata)
xdatacos
x_interpol=[-3, -1.5, 0, 1.5, 3]
y_interpol=np.cos(x_interpol)
f = interp1d(x_interpol, y_interpol)
f2 = interp1d(x_interpol, y_interpol,kind='cubic')

xnew = np.linspace(-3, 3, num=41, endpoint=True)
plt.plot(x_interpol, y_interpol, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()



#task 3.2  Interpolation
f = interp1d(xdata, xdatacos)
f2 = interp1d(xdata, xdatacos,kind='cubic')

xnew = np.linspace(-3, 3, num=95, endpoint=True)#set interpolation points
plt.plot(xdata, xdatacos, 'o', xnew, f(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.title('Linear and Cubic Spine Interpolation for 95 points from original dataset ')
plt.show()
f(xnew)




#Task 3.3
#for linear interpolation

H=pd.DataFrame(xdata)

H=H[H[0]<=3]
H=H[H[0]>=-3]
ytruevalue=np.cos(H)
yinterpol=pd.DataFrame(f(xnew))

ytruevalue.index = range(len(ytruevalue))
REMS=np.sqrt(((yinterpol-ytruevalue)*(yinterpol-ytruevalue)).sum()/95)
print('The root mean square error for linear interpolation is:',REMS)
#for cubic interpolation
yinterpol1=pd.DataFrame(f2(xnew))
REMS1=np.sqrt(((yinterpol1-ytruevalue)*(yinterpol1-ytruevalue)).sum()/95)
print('The root mean square error for cubic interpolation is:',REMS)




#task 3.4 Evaluate the dependence of the RMSE on the interpolation grid points
measurement=[-3, -1, 1, 3]
measurement1=[-3.14, -1.64, -0.14, 1.36, 2.86]
y_mea=np.cos(measurement)
y_mea1=np.cos(measurement1)

xnew = np.linspace(-3.14, 2.86, num=101, endpoint=True)
ynew=np.cos(xnew)
xnew1 = np.linspace(-3, 3, num=95, endpoint=True)
ynew1=np.cos(xnew)
f_linear = interp1d(measurement, y_mea)
f_cubic = interp1d(measurement, y_mea,kind='cubic')
#interpolation for five grid points
f_linear1 = interp1d(measurement1, y_mea1)
f_cubic1 = interp1d(measurement1, y_mea1,kind='cubic')
#calculate rems for linear and cubic interpolation for 4 grid points
yi1=pd.DataFrame(ynew1)-pd.DataFrame(f_linear(xnew1))
yi2=pd.DataFrame(ynew1)-pd.DataFrame(f_cubic(xnew1))
REMS1=np.sqrt((yi1*yi1).sum()/101)
REMS2=np.sqrt((yi2*yi2).sum()/101)
print('The root mean square error(4 grid points) for linear interpolation is:',REMS1)
print('The root mean square error(4 grid points) for cubic interpolation is:',REMS2)

#calculate rems for linear and cubic interpolation for 5 grid points
yi11=pd.DataFrame(ynew)-pd.DataFrame(f_linear1(xnew))
yi22=pd.DataFrame(ynew)-pd.DataFrame(f_cubic1(xnew))
REMS3=np.sqrt((yi11*yi11).sum()/101)
REMS4=np.sqrt((yi22*yi22).sum()/101)
print('The root mean square error(5 grid points) for linear interpolation is:',REMS3)
print('The root mean square error(5 grid points) for cubic interpolation is:',REMS4)

plt.plot(measurement1, y_mea1, 'o', xnew, f_linear1(xnew), '-', xnew, f_cubic1(xnew), '--')
plt.title('Linear and cubic Interpolation for five grid points')
plt.show()
plt.plot(measurement, y_mea, 'o', xnew1, f_linear(xnew1), '-', xnew1, f_cubic(xnew1), '--')
plt.title('Linear and cubic Interpolation for four grid points')



#Task 3.5  Interpolation of the monthly surface temperature in Bremen
temperaturedataset=temps.sel(lat=53,lon=9)
monthlytemperaturedata=temperaturedataset.groupby('time.month').mean('time')#obtain monthly temperature anomaly
monthlytemperaturedata
monthlyxaxisdata=np.linspace(1,12,12)
interpolategrid=np.linspace(1,12,120)#interpolation points
monthlytemperaturedata.interp(month=interpolategrid,method='cubic').plot.line(label='cubic')#interpolate for monthly data
monthlytemperaturedata.interp(month=interpolategrid).plot(label='linear')
plt.scatter(np.linspace(1,12,12),np.array(monthlytemperaturedata),color='r',label='data')
plt.title('Interpolation of monthly time series in Bremen')
plt.legend()
