import os
import codecs

oriFile =codecs.open("D:\\Map\\0.json", "r", "utf-8")
s = oriFile.read()
for i in range(1,60):
    path = "D:\\Map\\" + str(i) +".json"
    newFile = codecs.open(path,"w","utf-8")
    newFile.write(s)
    newFile.close()
oriFile.close()
