a,b=map(int,input("Enter two numbers: ").split())
while(b!=0):
  reminder=a%b
  a=b
  b=reminder

print(a)