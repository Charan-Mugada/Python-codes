#The first repeated digit
n=int(input("Enter a number: "))
seen=set()
repeated=None
while(n!=0):
  digit=n%10
  if digit in seen:
    repeated=digit
    break
  seen.add(digit)
  n=n//10
if repeated is not None:
  print(f"The first repeated digit is: {repeated}")
else:
  print("No num is repeated")