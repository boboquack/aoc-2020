l=list(map(int,INPUT.split()))

for i in l:
    if 2020-i in l:
        print(i*(2020-i))
        break

for i in l:
    for j in l:
        if 2020-i-j in l:
            print(i*j*(2020-i-j))
            break
    else:
        continue
    break
