## use regex to get all word has 7 character from a dictionary
import sys
import re
import codecs
def main():
    # My code here
    oriDict =codecs.open("D:\\anhviet109K.txt", "r", "utf-8")
    typeNDict = 7
    pathNewDict = "D:\\5.txt"
    s = ""
    nDict = set()
    for line in oriDict:
        m = re.findall("@[a-zA-Z]{4} ",line)
        for match in m:
            word = match[1:len(match)-1].upper()
            print (word)
            nDict.add(word)
    m = list(nDict)
    m.sort()
    for word in m:
        s = s + word + ","
    newDict = codecs.open(pathNewDict,"w", "utf-8")
    newDict.write(s)
    oriDict.close()
    newDict.close()

    pass

if __name__ == "__main__":
    main()