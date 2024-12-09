s=INPUT.split()

w=len(s[0])
h=len(s)
s=[['.']*(w+2)]+[['.']+list(i)+['.'] for i in s]+[['.']*(w+2)]

d=[(0,1),(-1,1),(1,1),(1,0),(-1,0),(1,-1),(0,-1),(-1,-1)]
def change(s):
    t=[['.' for i in range(w+2)] for i in range(h+2)]
    for i in range(1,h+1):
        for j in range(1,w+1):
            c=0
            for a,b in d:
                c+=s[i+a][j+b]=='#'
            if s[i][j]=='#' and c>=4:
                t[i][j]='L'
            elif s[i][j]=='L' and c==0:
                t[i][j]='#'
            elif s[i][j]=='L' and c>0:
                t[i][j]='L'
            elif s[i][j]=='#' and c<4:
                t[i][j]='#'
    return t

t=[]
while t!=s:
    t=s
    s=change(t)
print(sum(i.count('#') for i in s))

s=INPUT.split()


w=len(s[0])
h=len(s)
s=[['.']*(w+2)]+[['.']+list(i)+['.'] for i in s]+[['.']*(w+2)]

def change(s):
    t=[['.' for i in range(w+2)] for i in range(h+2)]
    for i in range(1,h+1):
        for j in range(1,w+1):
            c=0
            for a,b in d:
                p=i
                q=j
                while p!=0 and p!=h+1 and q!=0 and q!=w+1:
                    p+=a
                    q+=b
                    if s[p][q]=='L':
                        break
                    if s[p][q]=='#':
                        c+=1
                        break
            if s[i][j]=='#' and c>=5:
                t[i][j]='L'
            elif s[i][j]=='L' and c==0:
                t[i][j]='#'
            elif s[i][j]=='L' and c>0:
                t[i][j]='L'
            elif s[i][j]=='#' and c<5:
                t[i][j]='#'
    return t

t=[]
while t!=s:
    t=s
    s=change(t)
print(sum(i.count('#') for i in s))
