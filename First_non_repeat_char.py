#First Non Repeated Character
n=input("Enter: ")
for ch in n:
  count=n.count(ch)
  if count==1:
    print(f"The First NON Repeated Char is '{ch}'")
    break
else:
  print("No Repeating Char Found")
