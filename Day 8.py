s=INPUT.split('\n')
l=[i.split() for i in s]
l=[[i[0],int(i[1])] for i in l]

v=[0]*len(l)
acc=0
i=0
while v[i]==0:
    v[i]=1
    x=l[i]
    if x[0]=='jmp':
        i+=x[1]
    elif x[0]=='acc':
        acc+=x[1]
        i+=1
    elif x[0]=='nop':
        i+=1
    else:
        print('aa')
        break
print(acc)



def run(l):
    #print(l)
    v=[0]*len(l)
    acc=0
    i=0
    while v[i]==0:
        v[i]=1
        x=l[i]
        if x[0]=='jmp':
            i+=x[1]
        elif x[0]=='acc':
            acc+=x[1]
            i+=1
        elif x[0]=='nop':
            i+=1
        elif x[0]=='zzz':
            return [True,acc]
        else:
            print('aa')
            break
    return [False,acc]

for i in range(len(l)):
    r=[x[:] for x in l]
    if l[i][0]=='jmp':
        r[i][0]='nop'
        y=run(r)
        if y[0]:
            print(y[1])
            break
    if l[i][0]=='nop':
        r[i][0]='jmp'
        y=run(r)
        if y[0]:
            print(y[1])
            break

s='''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''.split('\n')
l=[i.split() for i in s]
l=[[i[0],int(i[1])] for i in l]
