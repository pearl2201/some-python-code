import os
import re
folder = "D:/Vocal alphabet"
folder2 = "D:/p2"

for f in os.listdir(folder):
	for filename in os.listdir(folder + "/" + f):
		print (filename)
		if (re.match('^[1-9]',filename)!=None):
			os.rename(folder + "/" + f + "/" + filename,folder2 +"/" + f + filename)


# for f in os.listdir(folder2):
# 	print (f)
# 	os.rename(folder2 + "/" + f, folder2 + "/" +  f[:1]+".mp3")			
