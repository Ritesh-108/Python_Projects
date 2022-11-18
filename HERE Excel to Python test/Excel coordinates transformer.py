#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as PD
import warnings
warnings=warnings.filterwarnings('ignore')
CSV=input('Enter filename in format "filename.csv" :')
DF=PD.read_csv(CSV)
DF[['Right','Left']]=DF['features.geometry.coordinates'].str.split(",",n=1,expand=True)
DF['Left']=DF['Left'].str.replace("]",',')
DF['features.geometry.coordinates.updated']=DF['Left']+DF['Right']
DF['features.geometry.coordinates.updated']=DF['features.geometry.coordinates.updated'].str.replace("[",'')
DF.drop(['Right','Left'],axis=1,inplace=True)
DF['features.geometry.coordinates']=DF['features.geometry.coordinates.updated'].str.strip()
DF.drop(['features.geometry.coordinates.updated'],axis=1,inplace=True)
DF.rename(columns = {'Unnamed: 0':' '}, inplace = True)
DF
D_F=input('Enter the updated filename you need in format "filename_updated.csv": ')
DF.to_csv(D_F,index=False)
print("Updation Successful")


# In[ ]:




