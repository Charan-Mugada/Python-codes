#To find the frequency of each char in a string(using dictionary)
'''s=input("enter a string: ")
d={}
for ch in s:
  if ch in d:
    d[ch]+=1
  else:
    d[ch]=1

for key, value in d.items():
  print(key,value)'''
#without dict

'''s=input("Enter a string: ")
l=[]
for ch in s:
  if ch not in l:
    count=0
    for ch2 in s:
      if ch==ch2:
        count+=1
    print(ch, count)
    l.append(ch)'''

#using set

s=input("Enter a string: ")
l=set()
for ch in s:
  if ch not in l:
    l.add(ch)
    m= s.count(ch)
    print(ch,m)

  


