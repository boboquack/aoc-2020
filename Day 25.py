x=int(INPUT.split()[0])
y=int(INPUT.split()[1])

m=20201227

n,o,t,u=1,0,0,0
while t==0 or u==0:
 n*=7
 n%=m
 o+=1
 if n==x and t==0:t=o
 if n==y and u==0:u=o
print(pow(7,t*u,m))
