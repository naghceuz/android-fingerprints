#analyze
#and for methodcallsthesame, 
#it doesnt help us unless we know what the values are
import os
import sys


thefile1 = str(sys.argv[1])

print "argument 1", str(sys.argv[1])
print "argument 2", str(sys.argv[2])

thefile2 = str(sys.argv[2])

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
samefunctionsamevalue = open("same-function-same-value.txt", "w")
samefunctiondifferentvalueValueinFile1 = open("samefunctiondifferentvaluethevalueinFile1.txt", "w")
samefunctiondifferentvalueValueinFile2 = open("samefunctiondifferentvaluethevalueinFile2.txt", "w")


samefunctionsamevalue.writelines("#This is the file which contain the same function with same value between file1 and file2 ")
samefunctiondifferentvalueValueinFile1.writelines("#This is the file1 which contain the same function but different value between file1 and file2 ")
samefunctiondifferentvalueValueinFile1.writelines("#and the value is from file1")


for line1 in file1N:
	if line1[0] = "#": 
		continue
	elif line1 in file2N:
		samefunctionsamevalue.write(line1);
	else:
		#goal 2: same function different value
		line1count = line1.split("=")
		line1count[0] += '\n'
		if line1count[0] in thefile2function:
			samefunctiondifferentvalueValueinFile1.write(line1)


samefunctiondifferentvalueValueinFile2.writelines("#This is the file1 which contain the same function but different value between file1 and file2 ")
samefunctiondifferentvalueValueinFile2.writelines("#and the value is from file2 ")




for line2 in file2N:
	if line2 in file1N:
		continue;
	else:
		#goal 2: same function different value
		line2count = line2.split("=")
		line2count[0] += '\n'
		if line2count[0] in thefile1function:
			samefunctiondifferentvalueValueinFile2.write(line2)




#goal 3: different function , different value, and only in file1
file3N = open("functionOnlyinFile1.txt", "w");

for line3 in file1N:
	theline3 = line3.split("=")
	theline3[0] += '\n'
	# for a in thefile2function:
	if theline3[0] in thefile2function:
		continue
	else:
		file3N.write(line3);


#goal 4:different function , different value , and only in file2
file4N = open("functionOnlyinFile2.txt", "w");

for line4 in file2N:
	theline4 = line4.split("=")
	theline4[0] += '\n'
	if theline4[0] in thefile1function:
		continue
	else:
		file4N.write(line4);


os.remove("file1function.txt")
os.remove("file2function.txt")


