s=INPUT.split('\n\n')

t=0
for i in s:
    t+=len(set(i.replace('\n','')))
print(t)

t=0
for i in s:
    j=i.split('\n')
    k=set(j[0])
    for l in j[1:]:
        k&=set(l)
    t+=len(k)
print(t)
