#Decision Tree
import pandas as pd
import math
import sys

def log2(x :float)->float:
    if x==0:
        #print("log 0")
        return 0
        
    else:
        return math.log2(x)

class DecTree:
    c_attr=None
    def __init__(self,data,class_attr,level=0):
        
        self.columns=list(data.columns)
        DecTree.c_attr=class_attr
        self.attr=self.get_attr(data)
        self.children={}
        self.level=level
        
        print(data)
        print("Current node attribute:",self.attr)
        
        if self.attr[0] in self.columns:
            self.set_attr(data)
        
    def __str__(self):
        childstr="".join(map(str,self.children.values()))
        corner=u"\u2514"
        line=u"\u2502"
        return  (self.level * ("     ") )+corner+\
            str(self.attr)+\
                (f"{str(list(self.children.keys()))}" if self.children.keys() else "<Leaf>" )+\
            "\n"+childstr
    
    #Method that finds info gain of all attributes and decides on
    #the best attribute   
    def get_attr(self,data :pd.DataFrame)->list:
        #Only one value for class attr 
        # that means the current node is a leaf node
        if len(data[DecTree.c_attr].unique())==1:
            return data[DecTree.c_attr].unique()
        
        #Some rare condition(maybe not so rare) 
        #where only one column left and the class attr
        #is not properly spread(confusing right check the eg)
        #attr class
        #HIGH YES
        #HIGH NO
        #here high has both no and yes and no remaining
        #columns to make the split so just choose the first class value

        if len(self.columns)==1:
            return list(data[DecTree.c_attr])[:1]

        #dict for storing info gain of each column    
        info_gain={}
        entropy=0
        
        #finding entropy
        for c_elem in data[DecTree.c_attr].unique():
            p=len(data[data[DecTree.c_attr]==c_elem])/len(data)
            entropy-=p*log2(p)
            
        #actual info gain finding part
        #split into two parts via ifelse
        #for numerical and nominal
        for i in self.columns:
            if i==DecTree.c_attr:
                #Bruh you dont need the info of the class attr
                continue
            if data.dtypes[i] in ['int64','float64']:
                info_gain[i]=self.numerical_gain(data,i)
                info_gain[i][-1]+=entropy
            else:
                info_gain[i]=self.nominal_gain(data,i)
                info_gain[i][-1]+=entropy
        

        max_gain_attr=max(info_gain,key=lambda x:info_gain[x][-1])
        #      Nominal                                                  Numerical
        return [max_gain_attr] if len(info_gain[max_gain_attr])==1 else [max_gain_attr,info_gain[max_gain_attr][0]]


    #Assigning children to this node 
    def set_attr(self,data :pd.DataFrame):
        #print(data.dtypes[self.attr[0]])
        remaining_columns=self.columns
        remaining_columns.remove(self.attr[0])
        
        #checking if attribute is continous
        if data.dtypes[self.attr[0]] in ['int64','float64']:
            #top half data set to one child and bottom half to other
            self.children['<=']=DecTree(data.loc[data[self.attr[0]]<=self.attr[1],remaining_columns],DecTree.c_attr,self.level+1)
            self.children['>']=DecTree(data.loc[data[self.attr[0]]>self.attr[1],remaining_columns],DecTree.c_attr,self.level+1)
        else:
            #print("set_attr",data.loc[data[self.attr[0]]==i,remaining_columns])
            #Splitting dataset based on class attrs value and creating new child for each partition
            for i in data[self.attr[0]].unique():
                self.children[i]=DecTree(data.loc[data[self.attr[0]]==i,remaining_columns],DecTree.c_attr,self.level+1)

        
    
    #To find gain of an attr(nominal)
    def nominal_gain(self,data :pd.DataFrame,attr :str)->list:
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
        return [info]    
                
    #To find gain of an attr(numerical)    
    def numerical_gain(self,data :pd.DataFrame,attr :str)->list:
        info=[None,-sys.maxsize]
        values=sorted(list(data[attr]))
        midpoints=[]
        row_count=len(data)
        for i in range(len(values)-1):
            midpoints.append((values[i]+values[i+1])/2)
        #print(midpoints)

        for split_point in midpoints:
            top_count=len((data[data[attr]<=split_point]))
            bottom_count=len((data[data[attr]>split_point]))
            info_temp_top=info_temp_bottom=0

            for c_elem in data[DecTree.c_attr].unique():
                p_top=len(data[(data[DecTree.c_attr]==c_elem) &\
                     (data[attr]<=split_point)])/top_count
                info_temp_top+=p_top*log2(p_top)  

                p_bottom=len(data[(data[DecTree.c_attr]==c_elem) &\
                     (data[attr]>split_point)])/bottom_count
                info_temp_bottom+=p_bottom*log2(p_bottom)

            info_temp=(top_count/row_count)*info_temp_top+(bottom_count/row_count)*info_temp_bottom
            #print([split_point,info_temp])
            if info[1]<info_temp:
                info=[split_point,info_temp]
        return info


data=pd.read_csv("exp81.csv")

print(DecTree(data,'Class'))