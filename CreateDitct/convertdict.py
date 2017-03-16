import sys
import re
import codecs
oriDict =codecs.open("D:\\new.txt", "r", "utf-8")

s = ""

for line in oriDict:
    s = s+line.strip() + "\n"

print (s)
s.replace(",\n",",")
newDict = codecs.open("D:\\new1.txt","w", "utf-8")
newDict.write(s)
oriDict.close()
newDict.close()