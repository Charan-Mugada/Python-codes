#unique number
n=int(input("Enter a number to check unique or not: "))
flag=False
seen=set()
while(n!=0):
  digit=n%10
  if digit in seen:
    flag=True
    break
  seen.add(digit)
  n=n//10
if flag:
  print("Not Unique Number")
else:
  print("Unique Number")

