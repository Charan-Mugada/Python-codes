#The given sentence must contain all 26 alphabets
sen=input("Enter a sentence: ").lower()
unique=set()
for ch in sen:
  if ch.isalpha():
    if ch not in unique:
      unique.add(ch)

if len(unique)==26:
  print("Pangram")
else:
  print("Not a pangram")