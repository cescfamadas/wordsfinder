import pandas as pd
import numpy as np
df= pd.read_csv("diccionari.txt", delim_whitespace=True)
dt=df[df['tipus'].str.match('^NP.*')]
df=pd.merge(df,dt, indicator=True, how='outer').query('_merge=="left_only"').drop('_merge', axis=1)
df=df.drop_duplicates(subset='paraula', keep="last")
df['paraula']=df['paraula'].str.lower()
df['paraula']=df['paraula'].str.replace("ú","u")
df['paraula']=df['paraula'].str.replace("ù","u")
df['paraula']=df['paraula'].str.replace("à","a")
df['paraula']=df['paraula'].str.replace("è","e")
df['paraula']=df['paraula'].str.replace("é","e")
df['paraula']=df['paraula'].str.replace("ò","o")
df['paraula']=df['paraula'].str.replace("ó","o")
df["paraula"].to_csv("net.txt",index=False)