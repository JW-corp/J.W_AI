import matplotlib
matplotlib.use('Agg')
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


## 32K old 50 epoch default
#time = [2223.3251526355743, 1451.9124898910522, 1137.9917290210724, 1140.3619375228882, 1166.649931192398,1014.0974791049957,1353.4979276657104]

## 32K new 100 epoch default
#time = [3694.408791065216, 2829.7513008117676, 2580.9733810424805, 2276.055812358856, 2361.5011258125305,2221.3792428970337,2680.1628584861755]
#time_large=[2935.0999977588654,1908.1206185817719,1401.791358947754,1142.4294373989105,1132.5579342842102,1470.9383869171143]


## 8Kfix for speedup
#time=[258567.16841275874,160685.8866262436,85292.47870731354,25507.26446390152,15490.927917003632,8999.204348564148,5223.29126906395,2850.1766772270203,1731.3487522602081,1353.4979276657104]


#log scl 32K
#time = [2117.8648080825806,1450.6409270763397,1160.1696314811707,1022.107349872589,878.6063137054443,840.2194459438324]

#log scl 16K
#time = [2440.980729341507, 1764.3287065029144, 1551.672635793686, 1397.4543027877808, 1392.6179225444794,1300.065186738968]

#node=[64,128,256,512,1024,2048,4096]
#node_large=[128,256,512,1024,2048,4096]


## 32K Strong-scale  224x224 CP Large Kenel adam LR = 2e-03 Effective batch = 32K
#time_224=[166.53976332187653 ,101.92912660121918 ,70.34434948921204 ,56.16551579713821 ,58.91952322006225] # with 2048
#time_224=[166.53976332187653 ,101.92912660121918 ,70.34434948921204 ,56.16551579713821]
#node_224 = [128,256,512,1024]
#text_224 = ['128nodes','256','512','1024']

## 8batch Weak-scale 224x224 CP Large Kenel adam LR = 2e-03 
time_224 = [17308.84763431549 ,10376.94586956501 ,5391.960455553873 ,1655.170814064833 ,843.2272506788665 ,442.7881581390027 ,231.06603512048721 ,135.06157711029053] 
node_224 = [4,8,16,64,128,256,512,1024] 
text_224 = ['4nodes','8','16','64','128','256','512','1024'] 


## 32K Strong-scale6 4x64 DefaultNorm0 adam LR=8e-03 Strong scale
#time_64 = [52.64287549972534 ,34.76981614112854 ,26.27677938938141 ,23.179390041828157 ,26.423430993556977]
#node_64 = [64,128,256,512,1024]
#text_64 = ['64nodes','128','256','512','1024'] 


# 8batch Weak-scale 64x64 DefaultNorm0 LR=8e-03
time_64 = [4754.470872561137 ,2544.376339018345 ,1367.4141018159928 ,397.29915613889693 ,287.7252774953842 ,125.58801151514054 ,86.47991998195648 ,52.25830784082413]
node_64 = [4,8,16,64,128,256,512,1024] 
text_64 = ['4nodes','8','16','64','128','256','512','1024'] 





title='Training elapsed time'
plt.rc('xtick',labelsize=20)
plt.rc('ytick',labelsize=20)

fig,axs = plt.subplots(1,figsize=(12,7))
axs.plot(node_64,time_64,'--bo',color='royalblue',markersize=12,label='64x64')
axs.plot(node_224,time_224,'--bo',color='darkorange',markersize=12,label='224x224')
#axs.plot(node,time,'--bo',color='royalblue',markersize=12,label='Training time / epoch')

i=0
for x,y in zip(node_224,time_224):
	#plt.text(x-7,y-7,text[i],fontsize=20)
	plt.text(x,y,text_224[i],fontsize=20)
	i+=1
#i=0
#for x,y in zip(node_64,time_64):
#	#plt.text(x-7,y-7,text[i],fontsize=20)
#	plt.text(x,y,text_64[i],fontsize=20)
#	i+=1

#print( '1024 nodes are',1600.95 / 56.91568506240845,'times faster than GPU' )

#plt.text(800,130, 'GPU: 1660.95', fontsize=25,color='maroon',alpha=0.6)
#axs.set_title(title,fontsize=25)
axs.set_xlabel('Number of nodes',fontsize=25)
axs.set_ylabel('Time [sec]',fontsize=25)
axs.set_xticks([0,120,250,500,1000,1200])
axs.grid()
plt.legend(prop={'size':15})
plt.tight_layout()
#plt.show()
plt.savefig('time_per_epoch.png')
