

# file1 = open('oneplus.txt').readlines();
# file2 = open('google.txt').readlines();

# text_in_file1 = file1.readlines();
# for line in file1:
# 	print line


#First find the difference between function calls
# count the line numbers
countFile1 = 0
file1N = open('oneplus.txt', 'rb')
while True:
	buffer = file1N.read(8192*1024)
	if not buffer:
		break
	countFile1 += buffer.count('\n')
print "File 1 call functions:" , countFile1  
file1N.close()


countFile2 = 0
file2N = open('google.txt','rb')
while True:
	buffer = file2N.read(8192*1024)
	if not buffer:
		break
	countFile2 += buffer.count('\n')
print "File 2 call functions:" , countFile2
file2N.close()


# analyze the android.R$styleable function


text_word = 'R$styleable'
numberOfStyle1 = 0;
file1 = open('oneplus.txt').readlines();
for line in file1:
	if text_word in line:
		numberOfStyle1= numberOfStyle1+1
print "file 1 contain functions with R$styleable ", numberOfStyle1

numberOfStyle2 = 0;
file2 = open('google.txt').readlines();
for line in file2:
	if text_word in line:
		numberOfStyle2 = numberOfStyle2+1
print "file 1 contain functions with R$styleable ", numberOfStyle2


#the similarities between file 1 and file 2 in terms of function calls

# file1 = open('oneplus.txt').readlines();
# file2 = open('google.txt').readlines();
# for line in file1:
# 	print line
# 	for line in file2:
# 		print line

# with open('oneplus.txt') as f:
#     t1 = f.read().splitlines()

#     t1s = set(t1)

# with open('google.txt') as f:
#     t2 = f.read().splitlines()
#     t2s = set(t2)

# #in file1 but not file2
# print "Only in file1"
# for diff in t1s-t2s:
#     print t1.index(diff), diff

# #in file2 but not file1
# print "Only in file2"
# for diff in t2s-t1s:
#     print t2.index(diff), diff












