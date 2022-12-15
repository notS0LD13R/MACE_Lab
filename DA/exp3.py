def foo(a,b,c):return (a*b)/c

print("Enter the contigency table:")
cont_table=[[int(x) for x in input().split()] for _ in range(2)]
sumt=[cont_table[0][0]+cont_table[0][1],
cont_table[1][0]+cont_table[1][1],
cont_table[0][0]+cont_table[1][0],
cont_table[0][1]+cont_table[1][1]]
tot=sum(sumt[:2])
exp_table=[[foo(sumt[0],sumt[2],tot),foo(sumt[0],sumt[3],tot)],
[foo(sumt[1],sumt[2],tot),foo(sumt[1],sumt[3],tot)]]

chi=0
for i in range(2):
    for j in range(2):
        chi+=(cont_table[i][j]-exp_table[i][j])**2/exp_table[i][j]

print("Chi square value:",chi)
if chi>float(input("Input table value:")):print("Data is dependent")
else:print("Data is independent")

a=[int(x) for x in input("Enter values in first attribute").split()]
b=[int(x) for x in input("Enter values in second attribute").split()]

meana,meanb=sum(a)/len(a),sum(b)/len(b)
vara,varb=sum([(xi-meana)**2 for xi in a])/len(a),sum([(xi-meanb)**2 for xi in b])/len(b)
vara,varb=vara**0.5,varb**0.5

r=0
for i in range(len(a)):
    r+=((a[i]-meana)*(b[i]-meanb))/(len(a)*vara*varb)

print("Correlaion coeff:",r)
