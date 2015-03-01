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






# #Goal 3: uniqueFunctioninFile1.txt uniqueFunctioninFile2.txt uniqueFunctioninFile3.txt
# # change compare to 

# a = len(sys.argv) - 1
# count = 1

# while(a>0):

# for line5 in:
# 	thelastfunction = open(str(sys.argv[count]),'rb').readlines();
# 	differentfunction = 
def compare2(list1 , list2):
	list6 = []
	for line1 in list1:
		if line1 in list2:
			continue
		else:
			list6.append(line1)
	return list6



for x in range(1,len(sys.argv)):
	x2 = (x + 1) % (len(sys.argv) - 1)
	a2 = len(sys.argv) - 2
	count = x2
	thenew3 = open(str(sys.argv[x]),"rb").readlines()

	while (a2>0):
		newlist = open(str(sys.argv[count]),'rb').readlines()
		thenew3 = compare2(thenew3, newlist)
		a2 = a2 - 1
		count = (count + 1) % (len(sys.argv) - 1)

	#write into the samefunctionsamevalue
	difffunctionsamevalue = open("uniquefunctioninfile" + str(x) +".txt","w")
	for line8 in thenew3:
		difffunctionsamevalue.writelines(line8)











