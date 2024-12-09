s=[int(i) for i in INPUT.split('\n')]

def v(l,n):
    for i in range(25):
        for j in range(i+1,25):
            if l[i]+l[j]==n:
                return True
    return False

i=0
while v(s[i:i+25],s[i+25]):i+=1
print(s[i+25])

n=s[i+25]

for i in range(len(s)):
    for j in range(i+2,len(s)+1):
        if sum(s[i:j])==n:
            print(max(s[i:j])+min(s[i:j]))
