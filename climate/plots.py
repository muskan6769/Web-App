from __main__ import *
import random
import numpy as np
import matplotlib.pyplot as plt

if time=="1900-2000":
        data=np.genfromtxt('1.csv',delimiter=',',dtype=None,skip_header=1,names=('year','Max_Temp','Min_Temp','Mean_Temp'))
        k=np.random.rand(100)
elif time=="2001-2016":
        data=np.genfromtxt('2.csv',delimiter=',',dtype=None,skip_header=1,names=('year','Max_Temp','Min_Temp','Mean_Temp'))
        k=np.random.rand(16)

if graph1=="line-graph":
    plt.plot(data['year'],data[name])

elif graph1=="scatter-plot":
    plt.scatter(data['year'],data[name],alpha=0.8,c=k)


elif graph1=="bar-graph":
    plt.bar(data['year'],data[name])

plt.title(name+' in India')
plt.ylabel("Temp in degree celcius")
plt.xlabel("year")
#plt.clf()
plt.show()