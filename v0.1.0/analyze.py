

file1 = open('oneplus.txt').readlines();
file2 = open('google.txt').readlines();


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
# according to Google SDK : 
# The android.R.styleable class and its fields were removed from the public API,
# to better ensure forward-compatibility for applications.
# The constants declared in android.R.styleable were platform-specific and subject to arbitrary change across versions, 
# so were not suitable for use by applications. You can still access the platform's styleable attributes from your resources or code. 
# To do so, declare a custom resource element using a in your project's res/values/R.attrs file, then declare the attribute inside. 
# For more information about custom resources, see Custom Layout Resources. 
# Note that the android.R.styleable documentation is still provided in the SDK, but only as a reference of the platform's styleable attributes for the various elements.









