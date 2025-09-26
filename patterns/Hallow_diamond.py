'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''
n=int(input("Enter: "))
for i in range(1,n+1):
  for j in range(1, n*2):
    if j == n - i + 1 or j == n + i - 1:
      print("*", end="")
    else:
      print(" ", end="")
  print()