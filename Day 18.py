s=INPUT.split('\n')

def val(s):
    #print(s)
    if '(' in s:
        j=s.index('(')
        t=1
        for i in range(j+1,len(s)):
            if s[i]=='(':
                t+=1
            elif s[i]==')':
                t-=1
                if t==0:
                    break
        u=val(s[j+1:i])
        return val(s[:j]+' '+str(u)+' '+s[i+1:])
    else:
        x=s.split()
        #print(x)
        acc=int(x.pop(0))
        while x:
            o=x.pop(0)
            p=int(x.pop(0))
            if o=='*':
                acc*=p
            elif o=='+':
                acc+=p
            else:
                print('Ooop',o)
                raise ValueError
        return acc

print(sum(val(t) for t in s))

def val(s):
    #print(s)
    if '(' in s:
        j=s.index('(')
        t=1
        for i in range(j+1,len(s)):
            if s[i]=='(':
                t+=1
            elif s[i]==')':
                t-=1
                if t==0:
                    break
        u=val(s[j+1:i])
        return val(s[:j]+' '+str(u)+' '+s[i+1:])
    elif '*' in s:
        j=s.index('*')
        return val(s[:j])*val(s[j+1:])
    else:
        x=s.split()
        return sum(int(i) for i in x[::2])

print(sum(val(t) for t in s))
