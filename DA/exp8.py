#Decision Tree
import pandas as pd
from math import log2
import sys

class DecTree:
    c_attr=None
    def __init__(self,data,class_attr):
        self.columns=data.columns
        DecTree.c_attr=class_attr
        self.attr=self.get_attr(data)
        self.children={}
    
    def get_attr(self,data):
        info_gain={}
        entropy=0
        for c_elem in data[DecTree.c_attr].unique():
            p=len(data[data[DecTree.c_attr]==c_elem])/len(data)
            entropy-=p*log2(p)
            
        
        for i in self.columns:
            if i==DecTree.c_attr:
                #Bruh you dont need the info of the class attr
                continue
            if data.dtypes[i] in ['int64','float64']:
                info_gain[i]=self.numerical_gain(data,i)
            else:
                info_gain[i]=self.nominal_gain(data,i)+entropy
        print(info_gain)
    

    def nominal_gain(self,data :pd.DataFrame,attr :str)->int:
        row_count=len(data)
        info=0
        for elem in data[attr].unique():
            elem_data=data[data[attr]==elem]
            elem_count=len(elem_data)
            info_temp=0
            for c_elem in data[DecTree.c_attr].unique():
                p=len(elem_data[elem_data[DecTree.c_attr]==c_elem])/elem_count
                #print(p,attr,elem,c_elem)
                info_temp+=p*log2(p)
            info+=(elem_count/row_count)*info_temp
        #print(info)
        return info    
                
        
    def numerical_gain(self,data :pd.DataFrame,attr :str)->list:
        info=[None,-sys.maxsize]
        values=sorted(list(data[attr]))
        midpoints=[]
        row_count=len(data)
        for i in range(len(values)-1):
            midpoints.append((values[i]+values[i+1])/2)
        print(midpoints)

        for split_point in midpoints:
            top_count=len((data[data[attr]<=split_point]))
            bottom_count=len((data[data[attr]>split_point]))
            for c_elem in data[DecTree.c_attr].unique():
                p=len(data[data[DecTree.c_attr]==c_elem and data[attr]<split_point])/1
        return info


data=pd.read_csv("exp8.csv")
#print(data[data['INCOME']=='HIGH'])
DecTree(data,'BUY')