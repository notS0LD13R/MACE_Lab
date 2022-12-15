#Decision Tree
import pandas as pd

class DecTree:
    def __init__(self,data):
        self.attr=self.get_attr(data)
        self.columns=data.columns
        self.children={}
    def get_attr(self,data):
        info_gain={}
        for i in self.columns:
            if data.dtype[i] in ['int64','float64']:
                info_gain[i]=self.numerical_gain(data,i)
            else:
                info_gain[i]=self.nominal_gain(data,i)
    def nominal_gain(self,data,attr):
        pass
    def numerical_gain(self,data,attr):
        pass


data=pd.read_csv("exp8.csv")
print(data.columns)

DecTree(data)