s=INPUT.split('\n\n')

l1=[int(i) for i in s[0].split()[2:]]
l2=[int(i) for i in s[1].split()[2:]]

while len(l1)!=0!=len(l2):
    c1=l1.pop(0)
    c2=l2.pop(0)
    if c1>c2:
        l1.append(c1)
        l1.append(c2)
    else:
        l2.append(c2)
        l2.append(c1)

x=l1
if len(x)==0:x=l2

print(sum((len(x)-i)*x[i] for i in range(len(x))))

l1=[int(i) for i in s[0].split()[2:]]
l2=[int(i) for i in s[1].split()[2:]]

def hash(l1,l2):
    return f'{repr(l1)}{repr(l2)}'

def rc(l1,l2):
    prev=set()
    while len(l1)!=0!=len(l2) and hash(l1,l2) not in prev:
        prev.add(hash(l1,l2))
        c1=l1.pop(0)
        c2=l2.pop(0)
        if len(l1)>=c1 and len(l2)>=c2:
            win=rc(l1[:c1],l2[:c2])[0]
            if win==1:
                l1.append(c1)
                l1.append(c2)
            else:
                l2.append(c2)
                l2.append(c1)
        else:
            if c1>c2:
                l1.append(c1)
                l1.append(c2)
            else:
                l2.append(c2)
                l2.append(c1)
    if len(l1)==0:
        return [2,l2]
    else:
        return [1,l1]

x=rc(l1,l2)[1]

print(sum((len(x)-i)*x[i] for i in range(len(x))))
