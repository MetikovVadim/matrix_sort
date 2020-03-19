#!/usr/bin/python
import sys,array,os
a=0
b=0
assert array.array('i').itemsize == 4
c = array.array('i')
word=""
f = open("matrix50kX50k.csv","r")
g = file('binary.numbers','wb')
limit = os.fstat(f.fileno()).st_size
while True: 
 if a == limit:
  break;
 byte = f.seek(a)
 res = f.read(1)
 a = a + 1 # print(res)
 if res == "\n":
    res = " "
 if res !="\r":
  if res !=" ":
   word=word+res
  else:
#   print word
#   int(word).tofile(g)
   if word != "":
    b=int(word)
    c.append(b)
#   g.write(b)
    c.tofile(g)
#   print(b)
    del c[:]
   else:
    print(".")
   word = ""
g.close()
