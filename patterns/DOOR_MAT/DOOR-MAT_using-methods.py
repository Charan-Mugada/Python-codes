n1,n2=map(int,input().split())
for i in range(1,n1,2):
    print(('.|.'*i).center(n2,'-'))
print('WELCOME'.center(n2,'-'))
for i in range(n1-2,0,-2):
    print(('.|.'*i).center(n2,'-'))