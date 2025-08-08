#Checking Prime Number Or Not
n=int(input("Enter a NUmber: "))
count=0
for i in range(1,n+1):
  if n%i==0:
    count+=1

if count==2:
  print("The given number is a prime number")
else:
  print("The given number is not a prime")

