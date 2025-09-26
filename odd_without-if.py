'''n=int(input())
odds=[i for i in range(1,n+1) if i%2!=0]
print(*odds)'''



n=int(input("Enter: "))
for i in range(1,n+1,2):
  print(i,end=' ')
