l=INPUT.split()

f=lambda s:(s[0],int(s[1:]))
l=[f(i) for i in l]

rot={0:(1,0),90:(0,1),180:(-1,0),270:(0,-1)}
r=0
x=0
y=0
for i in l:
    if i[0]=='N':
        y+=i[1]
    elif i[0]=='E':
        x+=i[1]
    elif i[0]=='S':
        y-=i[1]
    elif i[0]=='W':
        x-=i[1]
    elif i[0]=='F':
        a,b=rot[r]
        x+=a*i[1]
        y+=b*i[1]
    elif i[0]=='L':
        r=(r+i[1])%360
    elif i[0]=='R':
        r=(r-i[1])%360
print(abs(x)+abs(y))

wx=10
wy=1
x=0
y=0
for i in l:
    if i[0]=='N':
        wy+=i[1]
    elif i[0]=='E':
        wx+=i[1]
    elif i[0]=='S':
        wy-=i[1]
    elif i[0]=='W':
        wx-=i[1]
    elif i[0]=='F':
        x+=wx*i[1]
        y+=wy*i[1]
    elif i[0]=='L':
        if i[1]%360==90:
            wx,wy=-wy,wx
        elif i[1]%360==180:
            wx,wy=-wx,-wy
        elif i[1]%360==270:
            wx,wy=wy,-wx
    elif i[0]=='R':
        if i[1]%360==90:
            wx,wy=wy,-wx
        elif i[1]%360==180:
            wx,wy=-wx,-wy
        elif i[1]%360==270:
            wx,wy=-wy,wx
print(abs(x)+abs(y))
