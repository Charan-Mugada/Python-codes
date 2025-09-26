'''
*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
 
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
'''

n=int(input("Enter: "))
for i in range(1,n+1):
  print('* '*i,end='\n')
print()
for j in range(n,0,-1):
  print('* '*j,end='\n')