n1,n2=map(int,input("Enter a number: ").split())
l1=[]
l2=[]
max1=0
for i in range(1,n1+1):
  if n1%i==0:
    l1.append(i)
for j in range(1,n2+1):
  if n2%j==0:
    l2.append(j)

for i in l1:
    for j in l2:
        if i == j and i > max1:
            max1 = i
print(f"The GCD is {max1}")



