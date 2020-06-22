try:
	     rev=0
	     while n>0:
	     	ln=n%10
	     	rev=rev*10+ln
	     	n=n/10
	     if rev==n:
	     	print('palindrome')
	     else:
	     	print('not palindrome')
except:
            print('failed to provide input')
finally:
           print('try block and except are finished ')
 