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
    def __init__(self,root :Node,items :list):
        self.root=root
        self.items=items
        self.pattbase={}
        for item in items:
            self.pattbase[item]=\
                self.pattern_base_gen(self.root,item)
            print(item,':-',self.pattbase[item])
        
        

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