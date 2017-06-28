
import sys

n = int(raw_input().strip())
s =raw_input().strip();
new_s=[]
k=int(raw_input().strip())

palabra=""
for i in s:
  if i.isalpha():
    if i.islower():
      palabra= palabra+chr(((ord(i)-97+k)%26)+97)
    else:
      palabra= palabra+chr(((ord(i)-65+k)%26)+65)
  else:
    palabra= palabra + i
print palabra
