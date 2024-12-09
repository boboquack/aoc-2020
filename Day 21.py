s=INPUT.split('\n')

ings=[]
alls=[]
for i in s:
    u=i.split(' (contains ')
    ings.append(set(u[0].split(' ')))
    alls.append(set(u[1][:-1].split(', ')))

allall=set(alls[0])
alling=set(ings[0])
for i in range(len(alls)):
    allall|=alls[i]
    alling|=ings[i]

d={i:set(allall) for i in alling}
e={i:0 for i in alling}
for i in range(len(ings)):
    for thing in ings[i]:
        e[thing]+=1
    for thing in alling-set(ings[i]):
        d[thing]-=alls[i]

print(sum(e[i] for i in d if len(d[i])==0))

f={}
while not all(len(d[i])==0 for i in d):
    for i in d:
        if len(d[i])==1:
            for j in d[i]:
                f[j]=i
            for k in d:
                d[k]-={j}
            d[i]=set()

z=[]
for i in sorted(f.keys()):
    z.append(f[i])
print(','.join(z))
