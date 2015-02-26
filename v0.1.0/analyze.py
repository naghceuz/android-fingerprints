#analyze
#and for methodcallsthesame, 
#it doesnt help us unless we know what the values are
import os
import sys

print "This is a python script to analyze the difference between two Andriod device(or emulator) finger-print \n"





# counters !
# a function to count number of function calls in a file 
def quickfunctioncounter(filename):
	#quick counter function
	countFile1 = 0
	anotherfile1 = open(filename, 'rb')
	while True:
		buffer = anotherfile1.read(8192*1024)
		if not buffer:
			break
		countFile1 += buffer.count('\n')
	print str(countFile1) + " function calls"
	anotherfile1.close()
	return countFile1
	# for line in anotherfile1:
	# 	countFile1 =  countFile1+1
	# print countFile1 
	# anotherfile1.close()


# input two files you want to comparsion
thefile1 = str(sys.argv[1])
thefile2 = str(sys.argv[2])



#pass the input file 3's name, thefile3 
# for example, same-function-same-value.txt
thefile3 = str(sys.argv[3])

#pass the input
#samefunctiondifferentvaluethevalueinFile1.txt
thefile4 = str(sys.argv[4])

#pass the input 
#samefunctiondifferentvaluethevalueinFile2.txt
thefile5 = str(sys.argv[5])

# #pass the input
# #functionOnlyinFile1.txt
# thefile6 = str(sys.argv[6])

# #pass the input
# #functionOnlyinFile2.txt
# thefile7 = str(sys.argv[7])



print "The two files you input is:"

print "argument 1", str(sys.argv[1])
print "argument 2", str(sys.argv[2])


file1N = open(thefile1, 'rb').readlines();
file2N = open(thefile2, 'rb').readlines();


def splitFuntionandValue(thefile, theNewFileName):
	fileNew = open(theNewFileName,'w')
	for line in thefile:
		thecuttenline = line.split("=")
		fileNew.write(thecuttenline[0]+ "\n")


#fileNew.write(thecuttenline[0]+ "\n")
#a file named file1function contains file1's all function
splitFuntionandValue(file1N, "file1function.txt");

#a file named file2function contains file2's all function
splitFuntionandValue(file2N, "file2function.txt");


thefile1function = open("file1function.txt", "rb").readlines()
thefile2function = open("file2function.txt", "rb").readlines()

#goal 1: same function same value
# samefunctionsamevalue = open("same-function-same-value.txt", "w")
#test 
samefunctionsamevalue = open(thefile3, "w")

samefunctiondifferentvalueValueinFile1 = open(thefile4, "w")
samefunctiondifferentvalueValueinFile2 = open(thefile5, "w")

#write comments for the same-function-same-value.txt file 
samefunctionsamevalue.writelines("#This is the file which contain the same function with same value between file1 and file2 \n")
samefunctionsamevalue.writelines("#The file1 is:"+ str(sys.argv[1]) +"\n")
samefunctionsamevalue.writelines("#The file2 is:"+ str(sys.argv[2]) +"\n")


#write comments for the samefunctiondifferentvaluethevalueinFile1.txt file 
samefunctiondifferentvalueValueinFile1.writelines("#This is the file1 which contain the same function but different value between file1 and file2 ")
samefunctiondifferentvalueValueinFile1.writelines("and the value is from file1 \n")

#process the line1 and line2
for line1 in file1N:
	if line1[0] == "#": 
		continue
	elif line1 in file2N:
		samefunctionsamevalue.write(line1);
	else:
		#goal 2: same function different value
		line1count = line1.split("=")
		line1count[0] += '\n'
		if line1count[0] in thefile2function:
			samefunctiondifferentvalueValueinFile1.write(line1)


# samefunctiondifferentvalueValueinFile1
# quickfunctioncounter()

#goal 2: same function different value - branch for file2
samefunctiondifferentvalueValueinFile2.writelines("#This is the file1 which contain the same function but different value between file1 and file2 ")
samefunctiondifferentvalueValueinFile2.writelines("and the value is from file2 \n")

for line2 in file2N:
	if line2[0] == "#": 
		continue
	if line2 in file1N:
		continue;
	else:
		#goal 2: same function different value
		line2count = line2.split("=")
		line2count[0] += '\n'
		if line2count[0] in thefile1function:
			samefunctiondifferentvalueValueinFile2.write(line2)



#goal 3: different function , different value, and only in file1
file3N = open("functionOnlyinFile1", "w");
file3N.writelines("#This file contains the unique functions only in file1 \n")


for line3 in file1N:
	if line3[0] == "#": 
		continue
	else:
		theline3 = line3.split("=")
		theline3[0] += '\n'
		# for a in thefile2function:
		if theline3[0] in thefile2function:
			continue
		else:
			file3N.write(line3);


#goal 4:different function , different value , and only in file2
file4N = open("functionOnlyinFile2", "w");
file4N.writelines("#This file contains the unique functions only in file2 \n")


for line4 in file2N:
	if line4[0] == "#": 
		continue
	else:
		theline4 = line4.split("=")
		theline4[0] += '\n'
		if theline4[0] in thefile1function:
			continue
		else:
			file4N.write(line4);



#goal 5:  identify values that change, this will possibly identify variable 
#values across device we can use to autogenerate values

#files which are run at dfferent times but on same device 
# and indicate values that change. this will identify variable chaning values to the system

#input file1 and file2 
#to see among the same function they have , 
#compare 


#goal 6:specify output directory name at command line, place generated files in this directory



#remove the useless files
os.remove("file1function.txt")
os.remove("file2function.txt")


