n=int(input("Enter: "))
if n<=0:
  print("Enter positive number")
elif n==1:
  print("0")
else:
  a=0
  b=1
  print(a,b,end=' ')
  n-=2
  while(n!=0):
    sum1=a+b
    a=b
    b=sum1
    print(sum1,end=' ')
    n=n-1