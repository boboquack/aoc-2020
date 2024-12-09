c=[int(i) for i in INPUT]

cur=c[0]
for i in range(100):
    #print(c)
    x=c.index(cur)
    c=c[x:]+c[:x]
    a=c.pop(1)
    b=c.pop(1)
    d=c.pop(1)
    nex=cur-1
    if nex<min(c):nex=max(c)
    while nex in [a,b,d]:
        nex=nex-1
        if nex<min(c):nex=max(c)
    u=c.index(nex)
    c.insert(u+1,d)
    c.insert(u+1,b)
    c.insert(u+1,a)
    cur=c[1]

x=c.index(1)
c=c[x:]+c[:x]
print(''.join(str(i) for i in c[1:]))

r=[int(i)-1 for i in INPUT]

cups=[0]*1000000

for d in range(1000000):
    if d in r:
        u=r.index(d)
        if u==len(r)-1:
            cups[d]=len(r)
        else:
            cups[d]=r[u+1]
    elif d==999999:
        cups[d]=r[0]
    elif d==len(r):
        cups[d]=len(r)+1
    else:
        cups[d]=d+1

active=r[0]
for i in range(10000000):
    #if i%100000==0:print('...',i)
    c1=cups[active]
    c2=cups[cups[active]]
    c3=cups[cups[cups[active]]]
    c4=cups[cups[cups[cups[active]]]]
    
    cups[active]=c4

    new=active-1
    if new==-1:new=999999
    while new==c1 or new==c2 or new==c3:
        new-=1
        if new==-1:new=999999
    after=cups[new]
    
    cups[new]=c1
    cups[c3]=after
    
    active=cups[active]

print((cups[0]+1)*(cups[cups[0]]+1))
