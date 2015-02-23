#analyze2

thefile1 = 'Google-emulator.txt'
thefile2 = 'oneplus.txt'


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
	# for line in anotherfile1:
	# 	countFile1 =  countFile1+1
	# print countFile1 
	# anotherfile1.close()



print "Overview: "
print "File 1 has function numbers:" , quickfunctioncounter(thefile1)
print "File 2 has function numbers:" , quickfunctioncounter(thefile2)
print

# goal 1: (1) listing field/method calls the same in each,
#generate 2 new files 

file1N = open(thefile1, 'rb').readlines();
file2N = open(thefile2, 'rb').readlines();


#generate a new file
anotherfile1 = open("methodonlyinfile1.txt", "w")

# thisfile1 = file1.readlines()
for line1 in file1N:
	#write all the method without given a value into methodinfile1.txt
	thecuttenline = line1.split("=")
	anotherfile1.writelines(thecuttenline[0]+ "\n")
	


#generate another file called methodonlyinfile2
anotherfile2 = open("methodonlyinfile2.txt", "w")

# thiefile2 = file2.readlines()
for line2 in file2N:
	thecuttenline2 = line2.split("=")
	anotherfile2.writelines(thecuttenline2[0]+ "\n")
	

anotherfile1 = open("methodonlyinfile1.txt","rb").readlines()
anotherfile2 = open("methodonlyinfile2.txt","rb").readlines()



#generate a new file
methodcallsthesame = open("methodcallsthesame.txt", "w")

for line3 in anotherfile1:
	if line3 in anotherfile2:
		methodcallsthesame.writelines(line3)


print "File1 and File2 has", quickfunctioncounter("methodcallsthesame.txt"), "  the same in each"
print "They are saved in methodcallsthesame.txt"









	# if thecuttenline[0] in file2N: 
	# 	print "sucess"
	# if line1 in file2N: 
	# 	print "sucess"

	# if line1 in file2N:
	# 	file1.write(line1)



#goal 2: (2) feidl/method calls that also had the same values 

file1N = open(thefile1, 'rb').readlines();
file2N = open(thefile2, 'rb').readlines();

file2 = open("methodcallsamevalue.txt", "w")
for line2 in file1N:
	if line2 in file2N:
		file2.write(line2)

print
print "File1 and File2 has", quickfunctioncounter("methodcallsamevalue.txt"), " that also had the same values "
print "They are saved in methodcallsamevalue.txt"
print



# #goal 3: (3) method/field calls only in file 1 



print "File1 and File2 has", quickfunctioncounter("methodonlyinfile1.txt"), " that also had the same values "
print "They are saved in methodonlyinfile1.txt"
print


# #goal 4  (4) method/field calls only in file 2

print "File1 and File2 has", quickfunctioncounter("methodonlyinfile2.txt"), " that also had the same values "
print "They are saved in methodonlyinfile2.txt"
