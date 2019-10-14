import numpy as np
import matplotlib.pyplot as plt

#this program is to calculate the strength of the wind turbine sections

R=0.2
Cl=1.5
X=4
B=2
n=100000
i=1
j=1

Ltip=0.18
Lroot=0.022

step=(Ltip-Lroot)/n

i=Lroot
r=[]

while i<=Ltip:
    r.append(i)
    i+=step

itr=1
for j in r:
    chord[itr]=((16*np.pi*j)/(B*Cl))*((np.sin((1/3)*np.arctan(R/(X*j))))**2)
    itr+=1
Area=[]
for i in range(len(chord)-1):
    Area[j+1]=(chord[i+1]+chord[i])/2 * step
    j+=1

itr=1

midr=[]
for i in range(len(r)-1):
    midr[itr]=(r[i]+r[i-1])/2
    itr+=1


midr=np.array(midr)
Area=np.array(Area)
chord=np.array(chord)
r=np.array(r)

wr=((3000/60)*2*np.pi)*(midr)
vrel=(wr**2+8**2)**0.5

momenttoal=0
lift=np.array()
moment=np.array()
for i in range(len(Area)):
    lift[i]=0.5*1.225*Area[i]*Cl*(vrel[i])**2
    moment=midr[i]+lift[i]
    momenttoal+=moment

Total_area=sum(Area)
Total_lift=sum(lift)
moment_root=sum(momenttoal)    






