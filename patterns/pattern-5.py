n=int(input("Enter: "))
for i in range(1,n+1):
  for k in range(n-i+1):
    print(" ",end=' ')
  for j in range(n-i+1,n+1):
    print(j,end=' ')
  print()

  '''
  Enter: 8
                8 
              7 8
            6 7 8
          5 6 7 8
        4 5 6 7 8
      3 4 5 6 7 8
    2 3 4 5 6 7 8
  1 2 3 4 5 6 7 8 
  '''