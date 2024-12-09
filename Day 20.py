s=INPUT.split('\n\n')

d={}
for i in s:
 i=i.split('\n')
 u=int(i[0].split()[1][:-1])
 d[u]=[list(j) for j in i[1:]]

def rot(a):
 h=len(a)
 w=len(a[0])
 return [[a[h-1-i][j] for i in range(h)] for j in range(w)]

def ref(a):
 return [list(reversed(i)) for i in a]

def til(a):
 return [a,rot(a),rot(rot(a)),rot(rot(rot(a))),ref(a),rot(ref(a)),rot(rot(ref(a))),rot(rot(rot(ref(a))))]

def edg(a):
 return {1:[i[0] for i in a],
         2:a[0],
         3:[i[-1] for i in a],
         4:a[-1]}

def best(e):
 if e>list(reversed(e)):
  return ''.join(e)
 return ''.join(list(reversed(e)))

def good(a):
 k=edg(a)
 return {i:best(k[i]) for i in k}

o={}
for i in d:
 for j in good(d[i]).values():
  try:o[j].append(i)
  except KeyError:o[j]=[i]

y=1
for i in d:
 q=good(d[i]).values()
 v=sum(len(o[j]) for j in q)
 if v==6:
  #print(i)
  y*=i
  t=d[i]
 #print(v)
 
print(y)

img=[[0]*12 for i in range(12)]

for i in til(t):
 if len(o[best(edg(i)[3])])==2 and len(o[best(edg(i)[4])])==2:
  img[0][0]=i
  break
else:print('error')

for i in range(1,12):
 x=best(edg(img[i-1][0])[4])
 a,b=o[x]
 if img[i-1][0] in til(d[a]):
  a=b
 for j in til(d[a]):
  if edg(j)[2]==edg(img[i-1][0])[4]:
   img[i][0]=j
   break
 else:print('error2')

for i in range(12):
 for j in range(1,12):
  x=best(edg(img[i][j-1])[3])
  a,b=o[x]
  if img[i][j-1] in til(d[a]):
   a=b
  for g in til(d[a]):
   if edg(g)[1]==edg(img[i][j-1])[3]:
    img[i][j]=g
    break
  else:print('error3')

m=[[0]*96 for i in range(96)]
for i in range(12):
 for j in range(12):
  for k in range(1,9):
   for l in range(1,9):
    pix=img[i][j][k][l]
    if 0!=m[i*8+k-1][j*8+l-1]!=pix:
     print('error4')
    m[i*8+k-1][j*8+l-1]=pix

monster=[list(i) for i in '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')]

#print(sum(i.count('#') for i in m))

for c in til(monster):
 h=len(c)
 w=len(c[0])
 for i in range(97-h):
  for j in range(97-w):
   for k in range(h):
    for l in range(w):
     if c[k][l]=='#' and m[i+k][j+l]=='.':break
    else:continue
    break
   else:
    for k in range(h):
     for l in range(w):
      if c[k][l]=='#':
       m[i+k][j+l]='o'

print(sum(i.count('#') for i in m))
