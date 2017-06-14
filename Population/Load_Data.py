# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Read data
popu1= pd.read_csv("../Data/PopulationData/API_SP.POP.TOTL_DS2_en_csv_v2.csv", sep=',') #check the sepeartion point
popu2= pd.read_csv( "../Data/PopulationData/Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2.csv",sep="," )


#Population: Is the overview of data.
popu1.dropna()
country_Name= popu1['Country Name'] # Take out the colum labeled "Country Name" : Type :Series
for i in range( 0 , len(country_Name)) :
    if country_Name[i] == 'Vietnam' :
        k=i

def DataCleanse(k):
    l=list()
    s= popu1.iloc[k,4:-1] #row k, from the 4th element to the end
    Population =np.array( s)
    Years = np.array( s.index)
    name = country_Name[k]
    l.append(name)
    l.append(Population)
    l.append(Years)
    return l

l=DataCleanse(k)
l1= DataCleanse(2)
l2= DataCleanse(70)
l3= DataCleanse(139)
l4= DataCleanse(210)
#Years= list( map( int, Years))

#plt.plot( Population, Years, label= 'Vietnam Population Evolution')
#plt.legend()
#plt.show()
plt.plot( l[2],l[1], label= l[0],color='r')

plt.plot( l1[2],l1[1], label= l1[0],color='blue')

plt.plot( l2[2],l2[1], label= l2[0],color='green')

plt.plot( l3[2],l3[1], label= l3[0],color='yellow')

plt.plot( l4[2],l4[1], label= l4[0],color='brown')

plt.legend()
#plt.savefig( 'Population.png', transparent="False") # save image
plt.show()