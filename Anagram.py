#eg listen==silent the chars must be same in both words
s1=input("Enter 1st word: ").lower()
s2=input("Enter 2nd word: ").lower()
d1={}
d2={}
for ch1 in s1:
  if ch1 in d1:
    d1[ch1]+=1
  else:
    d1[ch1]=1
for ch2 in s2:
  if ch2 in d2:
    d2[ch2]+=1
  else:
    d2[ch2]=1

if d1==d2:
  print("Anagram")
else:
  print("Not Anagram")
