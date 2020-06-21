a=int(input('enter value of a'))
b=int(input('enter value of b'))
c=int(input('enter value of c'))
if a==b and b==c and c==a:
	print('all are equal')
elif a==b or b==c or c==a:
	print(' two are equal')
else:
	print('not equal')