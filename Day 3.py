slope=INPUT.split()

n=len(slope[0])
s=0
t=0
u=0
v=0
for i in range(len(slope)):
    s+=slope[i][i*1%n]=='#'
    t+=slope[i][i*3%n]=='#'
    u+=slope[i][i*5%n]=='#'
    v+=slope[i][i*7%n]=='#'
w=0
for i in range(0,len(slope),2):
    w+=slope[i][i//2%n]=='#'
print(t)
print(s*t*u*v*w)
