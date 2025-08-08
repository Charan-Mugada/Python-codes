#Second Largest Number
num=list(map(int,input("Enter a list of numbers to find which is second largest: ").split()))
first=second=float('-inf')
for i in num:
  if i>first:
    second=first
    first=i
  elif i>second and i!=first:
    second=i
print(f"The Second Largest Number is {second}")
  