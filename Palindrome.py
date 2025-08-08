#palindrome
n=int(input("Enter a number: "))
orginal=n
rev=0
while(n!=0):
  digit=n%10
  rev=rev*10+digit
  n=n//10

if orginal==rev:
  print(f"The given Number is a palindrome")
else:
  print("The given number is not a palindrome")