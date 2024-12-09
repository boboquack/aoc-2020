s=INPUT.split('\n\n')

#s=''' input '''.split('\n\n')

def valid(n):
    for i in 'byr iyr eyr hgt hcl ecl pid'.split():
        if i not in n:
            return False
    return True

k=0
for i in s:
    k+=valid(i)
print(k)

def valid2(n):
    try:
        if 1920<=int(n['byr'])<=2002 and\
        2010<=int(n['iyr'])<=2020 and\
        2020<=int(n['eyr'])<=2030 and\
        ((n['hgt'][-2:]=='cm' and\
          150<=int(n['hgt'][:-2])<=193)or\
         (n['hgt'][-2:]=='in' and\
          59<=int(n['hgt'][:-2])<=76)) and\
        n['hcl'][0]=='#' and all(i in '0123456789abcdef' for i in n['hcl'][1:]) and\
        n['ecl'] in 'amb blu brn gry grn hzl oth'.split() and\
        n['pid'].isnumeric() and len(n['pid'])==9:
            return True
        return False
    except KeyError:
        return False

k=0
for i in s:
    j=eval('{"'+i.replace(':','":"').replace(' ','","').replace('\n','","')+'"}')
    k+=valid2(j)
print(k)
