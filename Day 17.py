s=[[list(i) for i in '''##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#..'''.split()]]

#s=[[list(i) for i in '''.#.
#..#
####'''.split()]]

w=len(s[0][0])
h=len(s[0])
v=1

u=[]
for i in [-1,0,1]:
    for j in [-1,0,1]:
        for k in [-1,0,1]:
            u.append([i,j,k])

def update(s,t,w,h,v):
    for i in range(v):
        for j in range(h):
            for k in range(w):
                z=0
                for a,b,c in u:
                    if 0<i+a<=v-2 and 0<j+b<=h-2 and 0<k+c<=w-2:
                        z+=s[i+a-1][j+b-1][k+c-1]=='#'
                y=(0<i<=v-2 and 0<j<=h-2 and 0<k<=w-2)
                #print(i,j,k,z,y)
                if y and s[i-1][j-1][k-1]=='#' and (z==3 or z==4):
                    t[i][j][k]='#'
                elif ((not y) or s[i-1][j-1][k-1]=='.') and z==3:
                    t[i][j][k]='#'

for i in range(6):
    w+=2
    h+=2
    v+=2
    t=[[['.']*w for i in range(h)] for i in range(v)]
    update(s,t,w,h,v)
    s=t
    #for i in s:
        #for j in i:
            #print(''.join(j))
        #print()
    #print()

x=0
for i in s:
    for j in i:
        for k in j:
            x+=k=='#'
print(x)

s=[[[list(i) for i in '''##.#####
#.##..#.
.##...##
###.#...
.#######
##....##
###.###.
.#.#.#..'''.split()]]]

#s=[[[list(i) for i in '''.#.
#..#
####'''.split()]]]

w=len(s[0][0][0])
h=len(s[0][0])
v=1
q=1

u=[]
for i in [-1,0,1]:
    for j in [-1,0,1]:
        for k in [-1,0,1]:
            for l in [-1,0,1]:
                u.append([i,j,k,l])

def update(s,t,w,h,v,q):
    for l in range(q):
        for i in range(v):
            for j in range(h):
                for k in range(w):
                    z=0
                    for a,b,c,d in u:
                        if 0<i+a<=v-2 and 0<j+b<=h-2 and 0<k+c<=w-2 and 0<l+d<=q-2:
                            #print(l,i,j,k,d,a,b,c,q,v,h,w)
                            z+=s[l+d-1][i+a-1][j+b-1][k+c-1]=='#'
                    y=(0<i<=v-2 and 0<j<=h-2 and 0<k<=w-2 and 0<l<=q-2)
                    #print(l,i,j,k,z,y)
                    if y and s[l-1][i-1][j-1][k-1]=='#' and (z==3 or z==4):
                        t[l][i][j][k]='#'
                    elif ((not y) or s[l-1][i-1][j-1][k-1]=='.') and z==3:
                        t[l][i][j][k]='#'

for i in range(6):
    w+=2
    h+=2
    v+=2
    q+=2
    #print('...',i,w,h,v,q,w*h*v*q)
    t=[[[['.']*w for i in range(h)] for i in range(v)] for i in range(q)]
    update(s,t,w,h,v,q)
    s=t
    #for k in s:
    #    for i in k:
    #        for j in i:
    #            print(''.join(j))
    #        print()
    #    print()
    #print('end')
x=0
for i in s:
    for j in i:
        for k in j:
            for l in k:
                x+=l=='#'
print(x)
