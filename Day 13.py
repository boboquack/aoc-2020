s=INPUT.split('\n')
s[0]=int(s[0])
s[1]=s[1].split(',')
b=999999
r=0
for i in s[1]:
    if i=='x':continue
    j=int(i)
    k=j-(s[0]%j)
    if k<b:
        r=k*j
        b=k
print(r)

def crt(cval,cmod,nval,nmod):
    return cval+((nval-cval)*pow(cmod,-1,nmod))%nmod*cmod

cval=0
cmod=int(s[1][0])
for i in range(1,len(s[1])):
    j=s[1][i]
    if j!='x':
        k=int(j)
        cval=crt(cval,cmod,-i,k)
        cmod*=k

print(cval)
