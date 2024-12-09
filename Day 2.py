l=INPUT.split('\n')
l=[i.split() for i in l]
s=0
for i in range(len(l)):
    x=[int(i) for i in l[i][0].split('-')]
    s+=x[0]<=l[i][2].count(l[i][1][0])<=x[1]
print(s)
s=0
for i in range(len(l)):
    x=[int(i) for i in l[i][0].split('-')]
    s+=(l[i][2][x[0]-1]==l[i][1][0])^(l[i][2][x[1]-1]==l[i][1][0])
print(s)
