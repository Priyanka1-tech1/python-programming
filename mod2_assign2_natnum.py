def natnum(n):
      sum=0
      if n<=0: 
          print("Enter positive number") 
      else: 
           while n>0:
                sum = sum+n
                n= n-1;    
           print("Sum of natural nums", sum)
natnum(6)