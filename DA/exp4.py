#Apriori

from itertools import combinations

def count(trans,x):
	value=0
	x=set(x)
	for i in trans:
		if x.issubset(i):value+=1
	return value

def beauty_print(li):
	print("-"*21)
	for i in li:
		s=" ".join(i[0])
		print(f"|{s: ^16}|{i[1]: <2}|")
	print("-"*21)
def apriori(trans,c,min_support,n):
    li=[]
    print(f"{n:>7} item set")
    for i in combinations(c,n):
    	if count(trans,i)>=min_support:
    		li.append((i,count(trans,i)))
    		#print(i,count(trans,i))
	if li==[]:
    	print("\tNILL")
    	return
    beauty_print(li)
    #print(li,n)
    apriori(trans,c,min_support,n+1)

file=open('exp4.txt','r')
transactions=[]
tid=[]
min_support=2

#input file into a list in list where each line is inputted as a list
for i in file.readlines():
    line=i.split()[:]
    key,val=line[0],set(line[1:])
    transactions.append(val)
    tid.append(key)

#Getting all the items
temp=set()
for i in transactions:
	temp=temp.union(i)
temp=sorted(list(temp))
apriori(transactions,temp,min_support,1)
