#name:analyzeMutiply.py
#author: Owen Zhang     time: Feb 28, 2015
#this script is going to analyze mutiply Android source code
#for example:if you do comparsion between three different files
# the input will be: oneplus.txt , google.txt , samsung.txt
# the output will be:
# output1: samefunctionsamevalue.txt   check
# output2: samefunctiondifferentvalueinFile1.txt 
# output3: samefunctiondifferentvalueinFile2.txt 
# output4: samefunctiondifferentvalueinFile3.txt
# 
# output5: uniquefunctioninfile1.txt
# output6: uniquefunctioninfile2.txt
# output7: uniquefunctioninfile2.txt

import os
import sys

def compare(list1 , list2):
	list3 = []
	for line1 in list1:
		if line1 in list2:
			list3.append(line1)
	return list3


#goal 1: samefunctionsamevalue.txt
a = len(sys.argv) - 2
count = 2
thenew = open(str(sys.argv[1]),"rb").readlines()

while (a>0):
	newlist = open(str(sys.argv[count]),'rb').readlines()
	thenew = compare(thenew, newlist)
	a = a-1
	count = count +1

#write into the samefunctionsamevalue
samefunctionsamevalue = open("samefunctionsamevalue.txt","w")
for line in thenew:
	samefunctionsamevalue.writelines(line)




#Goal 2:samefunctiondifferentvalueinFile1.txt samefunctiondifferentvalueinFile2.txt 

list4 = []
a = len(sys.argv) - 2
count = 2

inputFile1 = open(str(sys.argv[1]),"rb").readlines()
samefunctiondifferentvalueinFile1 = open("samefunctiondifferentvalueinFile1.txt",'w')

for line2 in inputFile1:
	thecutline = line2.split("=")
	thecutline[0] += "\n"
	list4.append(thecutline[0])


# make a big file which contains all the function
while(a>0):
	thenewlist = open(str(sys.argv[count]),'rb').readlines()
	print str(count)
	for line3 in thenewlist:
		thecutline2 = line3.split("=")
		thecutline2[0] += '\n'
		list4.append(thecutline2[0])
	a = a-1
	count = count +1

#now list4 contains all the function
# loop all the function in 

samefunctionsamevalue =  open("samefunctionsamevalue.txt","rb").readlines()

a = len(sys.argv) - 1
count = 1


while (a>0):
	if count ==2:
		print "tell me"
	anotherfile = open(str(sys.argv[count]),'rb').readlines();
	samefunctiondifferentvalue = open("samefunctiondifferentvalueinFile"+str(count)+".txt" ,'w')
	for line4 in anotherfile:
		if line4 in samefunctionsamevalue:
			continue
		else:
			thecuttenline4 = line4.split("=")
			thecuttenline4[0] += '\n'
			if thecuttenline4[0] in list4:
				print "yes"
				samefunctiondifferentvalue.writelines(line4);
	count = count +1
	a = a-1











