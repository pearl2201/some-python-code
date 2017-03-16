## use regex to get all word has 7 character from a dictionary
import sys
import re
import codecs

def main(): 
    # My code here
    oriDict =codecs.open("D:\\de.lxd", "r", "utf-8")
    typeNDict = 7
    pathNewDict = "D:\\de1.txt"
    s = ""
    nDict = set()
    for line in oriDict:
        m = re.findall("^[a-z]{4}$",line)
        for match in m:
            word = match.upper()
            print (word)
            nDict.add(word)
        m = re.findall("^[a-z]{4}",line)
        for match in m:
            word = match[0:len(match)-1].upper()
            print (word)
            nDict.add(word)
        m = re.findall("[a-z]{4}",line) 
        for match in m:
            word = match[1:len(match)-1].upper()
            print (word)
            nDict.add(word)
        m = re.findall("[a-z]{4}$",line)
        for match in m:
            word = match[1:len(match)-1].upper()
            print (word)
            nDict.add(word)
    m = list(nDict)
    m.sort()
    for word in m:
        s = s + word + "\n"
    newDict = codecs.open(pathNewDict,"w", "utf-8")
    newDict.write(s)
    oriDict.close()
    newDict.close()

    pass

if __name__ == "__main__":
    main()