s=input("Enter string: ").lower()
count=0
for ch in s:
  if ch in 'aeiou':
    count+=1

print(f"Total number of vowels are: {count}")
