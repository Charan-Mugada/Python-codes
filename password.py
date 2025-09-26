s=input("Enter password: ")
lower=upper=special=digit=0
for i in s:
  if i.islower():
    lower+=1
  elif i.isupper():
    upper+=1
  elif i.isdigit():
    digit+=1
  elif i in '!@#$%^&*-':
    special+=1

cond_count=sum([lower>0,upper>0,digit>0,special>0])

if cond_count==4:
  print('Strong')
elif cond_count==3:
  print('Moderate')
else:
  print('Weak')
