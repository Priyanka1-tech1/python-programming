n1=int(input('enter num1'))
n2=int(input('enter num2 '))
n3=int(input('enter num3'))
def largest_of_three():
       if n1>n2 and n1>n3:
	       l=n1
	       print('num1 is largest',l)	
       elif n2>n1 and n2>n3:
             l=n2
             print('num2 is largest',l)
       else:
  	       l=n3
  	       print('num3 is largest',l)
 
largest_of_three();
 
 
