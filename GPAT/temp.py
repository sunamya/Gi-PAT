# library
import matplotlib.pyplot as plt
 
# create data
names='Turbidity','pH','Temperature','Humidity'
size=[13.5,5.8,33,45]
 
# Create a circle for the center of the plot
'''my_circle=plt.Circle( (0,0), 0.7, color='white')
plt.pie(size, labels=names, wedgeprops = { 'linewidth' : 7, 'edgecolor' : 'white' },colors=['#dd6b4d','#2577B5','#7A92A3','#4da74d','#003F87','#008B00'])
p=plt.gcf()
p.gca().add_artist(my_circle)
plt.show()
p.savefig('factory/static/images/airplot.png')'''
plt.bar(names,size,color='#4da74d',edgecolor='#003F87',width=0.5)
plt.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
plt.savefig('factory/static/images/water.png')
plt.show()
'''import numpy as np
import matplotlib.pyplot as plt
x=['2011','2012','2013','2014','2015','2016']
y=[ [100,36,64,14,130,50], [120,25,75,25,140,45],[115,22,48,21,180,70],[132,45,78,78,133,68],[150,76,54,44,170,67],[150,55,45,23,177,80]]
#x=range(1,6)
#y=[ [1,4,6,8,9], [2,2,7,10,12], [2,8,5,10,6] ]
label=['CO','O3','NO2','SO2','PM10','PM2.5']
plt.stackplot(x,y, labels=label,colors=['#2577B5','#7A92A3','#4da74d','#003F87','#808A87','#008B00'])
plt.legend(loc='best')
plt.xlabel("YEAR")
plt.ylabel("Pollutant Value")
plt.savefig('factory/static/images/facplot.png')
plt.show()'''


