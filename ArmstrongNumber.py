n=int(input("Enter a number: "))
x=n
orginal=n
count=sum1=0
while(x!=0):
  count+=1
  x//=10
while(n!=0):
  digit=n%10
  sum1+=digit**count
  n//=10
if orginal==sum1:
  print("The given number is a Armstrong Number")
else:
  print("The given number is not a Armstrong Number")
