l=list(map(int,input("Enter a list of numbers: ").split()))
n=len(l)
for i in range(0,n-1):
  for j in range(0,n-i-1):
    if l[j]>l[j+1]:
      temp=l[j]
      l[j]=l[j+1]
      l[j+1]=temp
print(l)

'''nums = list(map(int, input("Enter numbers: ").split()))

# Ascending
print(sorted(nums))

# Descending
print(sorted(nums, reverse=True))'''
