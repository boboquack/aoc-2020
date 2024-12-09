s=INPUT.split()

d={'n':1j,'s':-1j,'e':1,'w':-1}

def val(l):
    v=0
    ns=2
    for i in l:
        v+=d[i]*ns
        ns=2-(i in 'ns')
    return v

l=[val(i) for i in s]

t=0
u=set()
for i in set(l):
    if l.count(i)%2==1:
        t+=1
        u.add(i)
print(t)

a=[val(i) for i in ['e','nw','ne','','sw','se','w']]
for z in range(100):
    #print(z,len(u))
    k={}
    for i in u:
        for j in a:
            try:
                k[i+j]+=1
            except KeyError:
                k[i+j]=1
            
    w=set()
    for i in k:
        if k[i]==2 and i not in u:
            w.add(i)
        if 1<k[i]<=3 and i in u:
            w.add(i)
    u=w

print(len(u))
