class Node:
    def __init__(self,value=None,freq=0,children={},parent=None) -> None:
        self.value=value
        self.freq=freq
        self.children=children
        self.parent=parent
    
    def __str__(self) -> str:
        temp="\n".join([str(x) for x in self.children.values()])
        childstr=" ".join(self.children.keys())
        return str(self.value)+":"+childstr+"\n"+temp
    
    def assign(self,item_set:list):
        if not item_set:return
        
        #print(self.value,"=>",self.children.keys(),"||",item_set)
        self.freq+=1
        if item_set[0] not in self.children:
            self.children[item_set[0]]= Node(value=item_set[0],freq=0,parent=self,children={})        
        self.children[item_set[0]].assign(item_set[1:])

        





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