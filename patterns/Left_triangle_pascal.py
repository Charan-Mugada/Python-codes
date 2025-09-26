'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i)*2,end='')
  print('* '*i,end='\n')
for j in range(1,n):
  print(' '*(j*2),end='')
  print('* '*(n-j),end='\n')
