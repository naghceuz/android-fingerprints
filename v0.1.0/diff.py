#script to diff between two file
#use library function: difflib.unified_diff   
#url: https://docs.python.org/2/library/difflib.html#difflib.unified_diff
#This python script will create a file to pint 
#out the difference between file 1 and file 2 

import difflib
import sys

with open('oneplus.txt', 'r') as file1:
    with open('samsung.txt', 'r') as file2:
    	with open('Report-oneplusVSsamsung','w') as file_out:
	        diff = difflib.unified_diff(
	            file1.readlines(),
	            file2.readlines(),
	            fromfile='file1',
	            tofile='file2',
	        )
	    	for line in diff:
	        	file_out.write(line)


