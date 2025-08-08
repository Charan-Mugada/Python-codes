n=int(input("Enter a Number: "))
if n<1:
  print("Not a Prime Number")
for i in range(2,int(n**0.5)+1):
  prime=True
  if n%i==0:
    prime=False

if prime:
  print("The given number is a prime number")
else:
  print("The given number is not a prime number")
