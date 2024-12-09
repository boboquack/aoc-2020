l=[int(i) for i in INPUT.split()]

l=[int(i) for i in '''47
... 90 lines omitted
92'''.split()]

l.sort()
l=[0]+l
n=len(l)
l.append(l[-1]+3)
a=0
b=0
for i in range(n):
    if l[i+1]-l[i]==1:
        a+=1
    elif l[i+1]-l[i]==3:
        b+=1
print(a*b)

l=[0,0]+l
v=[0]*(n+3)
v[2]=1
for i in range(n):
    if l[i+3]-l[i]<=3:
        v[i+3]+=v[i]
    if l[i+3]-l[i+1]<=3:
        v[i+3]+=v[i+1]
    if l[i+3]-l[i+2]<=3:
        v[i+3]+=v[i+2]
print(v[-1])
