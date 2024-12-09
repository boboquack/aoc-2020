s=INPUT.split('\n')

mem={}
for i in s:
    if i[1]=='a':
        mask=i[7:]
    else:
        i=i[4:]
        i=i.split('] = ')
        j=int(i[0])
        k=int(i[1])
        for i in range(len(mask)):
            if mask[-i-1]=='0':
                k&=2**64-1-2**i
            elif mask[-i-1]=='1':
                k|=2**i
        mem[j]=k
print(sum(mem.values()))

def adr(v):
    if len(v)==0:
        return [0]
    if v[0]==1:
        return [1+2*i for i in adr(v[1:])]
    if v[0]==0:
        return [2*i for i in adr(v[1:])]
    if v[0]=='x':
        k=adr(v[1:])
        return [1+2*i for i in k]+[2*i for i in k]

mem={}
for i in s:
    if i[1]=='a':
        mask=i[7:]
    else:
        i=i[4:]
        i=i.split('] = ')
        j=int(i[0])
        k=int(i[1])
        v=[0]*36
        for i in range(36):
            if mask[-i-1]=='0':
                v[i]=int(bool(2**i&j))
            elif mask[-i-1]=='1':
                v[i]=1
            else:
                v[i]='x'
        for i in adr(v):
            mem[i]=k

print(sum(mem.values()))
            
