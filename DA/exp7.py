from collections import Counter
from itertools import combinations

class Node:
    def __init__(self,value=None,freq=0,children={},parent=None,level=0) -> None:
        self.value=value
        self.level=level
        self.freq=freq
        self.children=children
        self.parent=parent
    
    def __str__(self) -> str:
        childstr=" ".join(map(str,self.children.values()))
        return (self.level * "       " )+\
            ("{"+str(self.value)+","+str(self.freq)+"}")+\
            "\n"+childstr
    
    def assign(self,item_set:list):
        if not item_set:
            self.freq+=1
            return
        
        self.freq+=1
        if item_set[0] not in self.children:
            self.children[item_set[0]]= \
            Node(value=item_set[0],parent=self,children={},level=self.level+1)        
        self.children[item_set[0]].assign(item_set[1:])


class FPTree:
    min_supp=None
    def __init__(self,root :Node,items :list,min_supp=2):
        self.root=root
        self.items=items
        FPTree.min_supp=min_supp
        self.pattbase={}
        self.condfp={}
        self.freqpatt={}
        for item in items:
            self.pattbase[item]=\
                self.pattern_base_gen(self.root,item)
            #print(item,':-',self.pattbase[item])
            
            self.condfp[item]=\
                self.cond_fptree_gen(self.pattbase[item])
            #print(item,':-',self.condfp[item])

            self.freqpatt[item]=\
                self.freq_patt_gen(self.condfp[item],item)
            #print(item,':-',self.freqpatt[item])    
    
    def display(self):

    
    def min_freq(self,items :list,freq :dict)->int:
        return min([freq[x] for x in items])
    
    def freq_patt_gen(self,condfp :Counter,curr :str)->list:
        if not condfp:
            return []
        items=condfp.keys()
        freqpatt=[]
        for i in range(1,len(items)+1):
            for j in combinations(items,i):
                freqpatt.append({'items':j+(curr,),'freq':self.min_freq(j,condfp)})
        return freqpatt


    def cond_fptree_gen(self,pattbase :dict)->Counter:
        pool=[]
        for patt in pattbase:
           pool.extend(patt['items']*patt['freq']) 
        
        pool=Counter(pool)
        for i in list(pool.keys()):
            if pool[i]<FPTree.min_supp:del pool[i]
        
        return pool
        
        

    def pattern_base_gen(self,root :Node,item :str) ->list:
        if root.value==item:
            patterns={'items':[],'freq':root.freq}
            root=root.parent
            while root.value!='null':
                patterns['items'].append(root.value)
                root=root.parent
            
            return [patterns] if patterns['items'] else []
        
        returnlist=[]
        for i in root.children.values():
            returnlist.extend(self.pattern_base_gen(i,item))
        
        return returnlist





fp=open("exp7.txt")



#Loading values from file to transaction dictionary
transactions=dict()
for i in fp.readlines():
    line=i.split()[:]
    key,val=line[0],line[1:]
    transactions[key]=val

#Finding frequency of each individual item
item_freq=dict()
for i in transactions.values():
    for j in i:
        if j not in item_freq:
            item_freq[j]=1
        else:
            item_freq[j]+=1

root=Node(value='null')

#Sorting all list in transactions according to item_freq
#Also adding the new list to fp growth tree via assign
for i in transactions:
    transactions[i].sort(key=lambda x:item_freq[x] ,reverse=True)
    root.assign(transactions[i])





print(item_freq)
print(transactions)

print(root)

FPTree(root,item_freq.keys())