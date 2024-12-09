s=INPUT.split('\n\n')

reg=s[0].split('\n')
strs=s[1].split()

d={}
p={}
for i in reg:
    if '"' in i:
        d[int(i.split(':')[0])]={i[-2]}
    else:
        j=i.split(': ')
        ind=int(j[0])
        u=j[1].split(' | ')
        p[ind]=[[int(k) for k in l.split()] for l in u]

while p:
    u=list(p.keys())
    for i in u:
        for j in p[i][0]+p[i][-1]:
            if j not in d:break
        else:
            d[i]=set()
            if len(p[i][0])==1:
                for j in d[p[i][0][0]]:
                    d[i].add(j)
            elif len(p[i][0])==2:
                for j in d[p[i][0][0]]:
                    for k in d[p[i][0][1]]:
                        d[i].add(j+k)
            elif len(p[i][0])==3:
                for j in d[p[i][0][0]]:
                    for k in d[p[i][0][1]]:
                        for l in d[p[i][0][2]]:
                            d[i].add(j+k+l)
            if len(p[i])==2:
                if len(p[i][0])==1:
                    for j in d[p[i][1][0]]:
                        d[i].add(j)
                else:
                    for j in d[p[i][1][0]]:
                        for k in d[p[i][1][1]]:
                            d[i].add(j+k)
            del p[i]

print(len([i for i in strs if i in d[0]]))

def match(i):
    if i=='':return True
    global d
    for d42 in d[42]:
        if i[:len(d42)]==d42 and match(i[len(d42):]):
            return True
        for d31 in d[31]:
            if len(d42)+len(d31)<=len(i) and \
               i[:len(d42)]==d42 and \
               i[-len(d31):]==d31 and \
               match(i[len(d42):-len(d31)]):
                return True
    return False

def match1(i):
    global d
    for d42 in d[42]:
        for d422 in d[42]:
            for d31 in d[31]:
                if len(d42)+len(d422)+len(d31)<=len(i) and \
                   i[:len(d42)]==d42 and \
                   i[len(d42):len(d42)+len(d422)]==d422 and \
                   i[-len(d31):]==d31 and \
                   match(i[len(d42)+len(d422):-len(d31)]):
                    return True
    return False

tot=0
for i in range(len(strs)):
    tot+=match1(strs[i])
    #print(i,tot)

print(tot)
