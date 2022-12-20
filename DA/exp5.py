#K Means Clustering

import matplotlib.pyplot as plt
import random

def point_generator(fp,count):
    fp=open(fp,'w')
    for i in range(count):
        fp.write(str(random.randint(0,100))+" "+str(random.randint(0,100))+"\n")
    fp.close()

def dist(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

def kmeans(points,centroid,k,l,prev_cluster=[]):
    print(f"\nIteration\n")
    cluster=[]
    
    #Heading of table
    a=""
    tempstr=f"|{a: <8}"
    for i in centroid:
        tempstr+=f"|{str([round(x,2) for x in i]): ^15}"
    tempstr+="|"
    print(tempstr)
    
    #Generating new cluster list assigning group no to each point
    #tempstr is related to table printing
    for i in range(l):
        minpos=0
        tempstr=f"|{str([round(i,2) for i in points[i]]): ^8}"
        for j in range(k):
            tempstr+=f"|{str(round(dist(points[i],centroid[j]),2)): ^15}"
            if dist(points[i],centroid[j])<dist(points[i],centroid[minpos]):
                minpos=j
        tempstr+="|"+str(minpos)+"|"
        print(tempstr)
        cluster.append(minpos)
    
    #checking if next iteration is needed or not
    if cluster==prev_cluster:
        return cluster
    else:
        for i in range(k):
            centroid[i]=[0,0]
        #generating new centroids
        for i in range(l):
            centroid[cluster[i]][0]+=points[i][0] #x
            centroid[cluster[i]][1]+=points[i][1] #y
        for i in range(k):
            centroid[i][0]/=max(cluster.count(i),1)
            centroid[i][1]/=max(cluster.count(i),1)
        return kmeans(points,centroid,k,l,cluster)

point_generator('exp5.txt',int(input("Enter no of points:")))

fp=open('exp5.txt','r')
points=[[int(y) for y in x.split()] for x in fp.readlines()]
print(points)
k=int(input("Enter the number of clusters:"))
centroids=points[:k]

groups=kmeans(points,centroids,k,len(points),centroids)


#plotting groups
X=[x[0] for x in points]
Y=[x[1] for x in points]
colors=['red','green','blue','yellow','orange']
plt.scatter(X,Y,color=[colors[i] for i in groups])
plt.show()

