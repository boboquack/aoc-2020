s=INPUT.split('\n')

d={}
for i in s:
    j=i.split(" contain ")
    j[0]=j[0].rstrip('s')
    if j[1]=='no other bags.':
        d[j[0]]={}
        continue
    k=j[1].split(', ')
    k=[z.rstrip('.').rstrip('s').split() for z in k]
    d[j[0]]={' '.join(z[1:]):int(z[0]) for z in k}
r={i:[] for i in d.keys()}
for i in d.keys():
    for j in d[i].keys():
        r[j].append(i)
vis={i:0 for i in d.keys()}
queue=['shiny gold bag']
vis['shiny gold bag']=1
done=0
while len(queue):
    x=queue.pop(0)
    for b in r[x]:
        if not vis[b]:
            done+=1
            vis[b]=1
            queue.append(b)
print(done)

t={i:0 for i in d.keys()}
n={i:0 for i in d.keys()}
m=len(d.keys())
while m>0:
    for i in d.keys():
        if t[i]==len(d[i].keys()):
            break
    else:
        print('?')
        break
    n[i]+=1
    t[i]+=1
    for b in r[i]:
        n[b]+=n[i]*d[b][i]
        t[b]+=1
    m-=1
print(n['shiny gold bag']-1)
    
