s=INPUT.split()

def seat(n):
	return int(n[:7].replace('B','1').replace('F','0'),2)*8+int(n[7:].replace('L','0').replace('R','1'),2)

print(max(seat(i) for i in s))

l=sorted([seat(i) for i in s])
for i in range(len(l)-1):
	if l[i+1]-l[i]==2:print(l[i]+1)
