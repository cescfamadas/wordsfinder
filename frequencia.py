import pandas as pd
import numpy as np
df= pd.read_csv("net.txt", delim_whitespace=True)
df=df[df.paraula.apply(lambda x: len(str(x))==5)]
df=df.sort_values('paraula')
df["1"]=df["paraula"].astype(str).str[0]
df["2"]=df["paraula"].astype(str).str[1]
df["3"]=df["paraula"].astype(str).str[2]
df["4"]=df["paraula"].astype(str).str[3]
df["5"]=df["paraula"].astype(str).str[4]

df["paraula"].to_csv("wordle.txt",index=False)

freqs=pd.DataFrame()
freqs["1"]=df["1"].value_counts()
freqs["2"]=df["2"].value_counts()
freqs["3"]=df["3"].value_counts()
freqs["4"]=df["4"].value_counts()
freqs["5"]=df["5"].value_counts()
freqs=freqs.sort_index()
print(freqs)
