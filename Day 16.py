s=INPUT.split('\n\n')

l=s[0].split('\n')
a=[]
d={}
for i in l:
 q=i.split(': ')
 r=q[1].split(' or ')
 d[q[0]]=[]
 for w in r:
  x=w.split('-')
  u=list(range(int(x[0]),int(x[1])+1))
  a+=u
  d[q[0]]+=u
  

t=0
m=s[2].split()[2:]
z=[]
for i in m:
 j=[int(k) for k in i.split(',')]
 n=True
 for o in j:
  if o not in a:
   t+=o
   n=False
 if n:
  z.append(j)
 
print(t)

e={i:[True for i in z[0]] for i in d}
for i in z:
 for j in range(len(i)):
  for q in d:
   if i[j] not in d[q]:
    e[q][j]=False

f={i:[] for i in d}
v=[int(i) for i in s[1].split()[2].split(',')]
for i in d:
 for j in range(len(e[i])):
  if e[i][j] and (v[j] in d[i]):
   f[i].append(v[j])

g=[0]*len(v)
i=0
for i in f.values():
 g[len(i)-1]=i

c=1
for i in range(1,len(v)):
 for j in f:
  if g[i]==f[j]:break
 b=list(set(g[i])-set(g[i-1]))[0]
 if j[:3]=='dep':c*=b
print(c)

