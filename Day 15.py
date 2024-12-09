l=list(map(int,INPUT.split()))

while len(l)<2020:
    x=l[-1]
    if x in l[:-1]:
        for i in range(2020):
            if l[-i-2]==x:
                l.append(i+1)
                break
    else:
        l.append(0)
print(l[-1])

l=list(map(int,INPUT.split()))

d={l[i]:i for i in range(len(l)-1)}
last=l[-1]

i=len(l)
while i<30000000:
    #if i%100000==0:print('...',i)
    try:
        x=i-d[last]-1
    except KeyError:
        x=0
    d[last]=i-1
    last=x
    i+=1
print(last)
