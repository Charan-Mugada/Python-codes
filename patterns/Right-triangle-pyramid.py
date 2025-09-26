'''
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i)*2,end='')
  for j in range(i):
    print('*',end=' ')
  print()
