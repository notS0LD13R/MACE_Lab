import pandas as pd
import numpy as np
import math

#Naïve Bayes

def equation(mean,variance,x):
    expon=math.exp(((-1)*(x-mean)**2)/(2*variance))
    return expon/(math.sqrt(2*math.pi)*mean)

def classify(unknown :pd.DataFrame,data :pd.DataFrame,cattr:str)->str:
    clss_prob={}
    row_count=len(data)
    
    #for each unique value in class attribute
    for clss in data[cattr].unique():
        clss_count=len(data[data[cattr]==clss])
        prob_ci=clss_count/row_count
        prob_xi=1
        
        #for each attribute except class
        for attr in unknown.columns:
            
            #For continous values else nominal
            if unknown.dtypes[attr] in ['int64','float64']:
                mean=data[data[cattr]==clss][attr].mean()
                variance=data[data[cattr]==clss][attr].var()
                prob_xi*=equation(mean,variance,unknown[attr][0])
                
            else:
                prob_xi*=len(data[(data[attr]==unknown[attr][0])&(data[cattr]==clss)])/clss_count

        clss_prob[clss]=prob_xi*prob_ci
    
    return max(clss_prob,key=lambda x:clss_prob[x])


data=pd.read_csv('exp8.csv')
unknown={}
for i,z in zip(data.columns[:-1],[30,'HIGH','NO','FAIR']):
    unknown[i]=[z]
unknown=pd.DataFrame(unknown)
print(unknown.iloc[0].tolist(),'is',classify(unknown,data,'BUY'))