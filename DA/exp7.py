from collections import Counter
from itertools import combinations


class Node:
    def __init__(self,value=None,freq=0,children={},parent=None,level=0) -> None:
        self.value=value
        self.level=level
        self.freq=freq
        self.children=children
        self.parent=parent
    #recursive tree printing
    def __str__(self) -> str:
        childstr="".join(map(str,self.children.values()))
        corner=u"\u2514"
        line=u"\u2502"
        return  (self.level * ("     ") )+corner+\
            ("{"+str(self.value)+","+str(self.freq)+"}")+\
            "\n"+childstr
    #Assigning children to current node based on item set
    def assign(self,item_set:list):
        #for leaf nodes freq to be incremented
        if not item_set:
            self.freq+=1
            return
        
        self.freq+=1
        #if the nodes already a child then skip the creation of new node
        if item_set[0] not in self.children:
            self.children[item_set[0]]= \
            Node(value=item_set[0],parent=self,children={},level=self.level+1)        
        #recursive call to assign children to child of current node
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
        
        #Finding conditonal pattern Base
        #Conditional FP Tree Frequent Patterns
        #for each item
        for item in self.items:
            self.pattbase[item]=\
                self.pattern_base_gen(self.root,item)
            #print(item,':-',self.pattbase[item])
            
            self.condfp[item]=\
                self.cond_fptree_gen(self.pattbase[item])
            #print(item,':-',self.condfp[item])

            self.freqpatt[item]=\
                self.freq_patt_gen(self.condfp[item],item)
            #print(item,':-',self.freqpatt[item]) 
        
        self.display()   

    def display(self):
        print("{: <4}|{: ^50}|{: ^25}|{: ^50}".format("item","Conditional Pattern Base","Conditional FP-tree","Frequent Patterns Generated"))
        print('-'*100)
        for item in self.items:
            cpline=""
            cfpline=""
            fpline=""
            for i in self.pattbase[item]:
                cpline+=\
                '{'+str(i['items'])+":"+str(i['freq'])+"}"+","

            cfpline=str(self.condfp[item])[7:]

            for i in self.freqpatt[item]:
                fpline+=\
                '{'+str(i['items'])+":"+str(i['freq'])+"}"+"," 
            print(f"{item: <4}|{cpline: ^50}|{cfpline: ^25}|{fpline: ^50}")

    #Used for finding the item with least frequency from a dict
    def min_freq(self,items :list,freq :dict)->int:
        return min([freq[x] for x in items])
    
    #Taking a counter(item and its freq dict) and
    #finding all combinations of items and adding the 
    #corresponding item set to its end
    #eg i1 i2 i3 for i5 gives i1i5,i2i5,i3i5,i1i2i5,i1i3i5 .....
    def freq_patt_gen(self,condfp :Counter,curr :str)->list:
        if not condfp:
            return []
        items=condfp.keys()
        freqpatt=[]
        for i in range(1,len(items)+1):
            for j in combinations(items,i):
                freqpatt.append({'items':j+(curr,),'freq':self.min_freq(j,condfp)})
        return freqpatt

    #Pooling the total number of items in each set into one big pool
    #then getting the frequencies of each item in pool
    def cond_fptree_gen(self,pattbase :dict)->Counter:
        pool=[]
        for patt in pattbase:
           pool.extend(patt['items']*patt['freq']) 
        
        pool=Counter(pool)
        
        #Excluding elements with freq<minimum suppourt
        for i in list(pool.keys()):
            if pool[i]<FPTree.min_supp:del pool[i]
        
        return pool
        
        
    #Starting at root and going down the tree
    #to specified item node
    #Then from the node moving up to its parents until null/root is reached
    #returning all the nodes it went through as a list
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





try:
    fp=open("exp7.txt")
except:
    print("File not found")
    exit()


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
    print(transactions[i])
    root.assign(transactions[i])



print(root)

FPTree(root,item_freq.keys())