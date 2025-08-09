#The given sentence must contain all 26 alphabets
import string
sen=input("Enter a sentence: ").lower()
unique=set()
allalpha=set(string.ascii_lowercase)
for ch in sen:
  if ch.isalpha():
    if ch not in unique:
      unique.add(ch)

missing=allalpha-unique

if len(unique)==26:
  print("Pangram")
else:
  print("Not a pangram missing letters are: ",",".join(sorted(missing)))