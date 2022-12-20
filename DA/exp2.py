#Dissimilarity Matrix
class Data:
    def __init__(self,file):
        self.file=open(file)
        self.table=[x[:-1].split() for x in self.file.readlines()]
        self.rowcount=len(self.table)
    
    def __str__(self):
        string=""
        for i in self.table:
            string+=" ".join(i)+'\n'
        return string
    
    def view(self,matrix,name=""):
        print(name)
        for j,i in enumerate(matrix):
            temp=" ".join(i[:j+1])
            print(temp)
    
    def nominaldiff(self,r1,r2,npos):
        p=len(npos)
        q=0
        for i in npos:
            if r1[i]==r2[i]:
                q+=1
        return str(round((p-q)/p,2))

    def numericaldiff(self,r1,r2,npos):
        dist=0
        for i in npos:
            dist+=(int(r1[i])-int(r2[i]))**2
        return str(round(dist**0.5,2))
    
    def prox(self,npos,option):
        matrix=[]
        for i in range(self.rowcount):
            matrix.append(['0']*self.rowcount)
        
        for i in range(self.rowcount):
            for j in range(i+1,self.rowcount):
                if option=="nominal":
                    matrix[i][j]=matrix[j][i]=\
                        self.nominaldiff(self.table[i],self.table[j],npos)
                if option=="numerical":
                    matrix[i][j]=matrix[j][i]=\
                        self.numericaldiff(self.table[i],self.table[j],npos)
        self.view(matrix,"--"+option+" matrix--")
        return matrix
        
obj=Data("exp2.txt")
print(obj)
obj.prox([0,1],'nominal')
obj.prox([2,3],'numerical')
        
