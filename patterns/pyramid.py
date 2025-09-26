'''          
     *
    ***
   *****
  *******
 *********
***********

'''
'''n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end='')
  print('*'*(2*i-1))'''

n=int(input("Enter: "))
for i in range(1,n+1):
  print(' '*(n-i),end=' ')
  print('* '*i,end=' ')
  print()

