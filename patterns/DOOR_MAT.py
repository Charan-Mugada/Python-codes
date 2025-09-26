'''
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''
n1,n2=map(int,input().split())
r=n2//n1
div=n2
wel=n2-7
for i in range(1,(n1//2)+1):
    div=div-r
    print('-'*(div//2),end='')
    print('.|.'*(2*i-1),end='')
    print('-'*(div//2),end='\n')
    div=div-r
print('-'*(wel//2),end='')
print('WELCOME',end='')
print('-'*(wel//2))
for i in range((n1//2),0,-1):
    div=div+r
    print('-'*(div//2),end='')
    print('.|.'*(2*i-1),end='')
    print('-'*(div//2),end='\n')
    div=div+r
    
    

    
    