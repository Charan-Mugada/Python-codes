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
  print('* '*i,end='\n')
for j in range(n-1,0,-1):
  print('* '*j,end='\n')