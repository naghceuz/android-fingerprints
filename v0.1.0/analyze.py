import string
import re



thefile1 = 'Google-emulator.txt'
thefile2 = 'samsung.txt'

print "Overview"

countFile1 = 0
file1N = open(thefile1, 'rb')
while True:
	buffer = file1N.read(8192*1024)
	if not buffer:
		break
	countFile1 += buffer.count('\n')
print thefile1, "has" , countFile1 , "function calls"
file1N.close()

countFile2 = 0
file2N = open(thefile2,'rb')
while True:
	buffer = file2N.read(8192*1024)
	if not buffer:
		break
	countFile2 += buffer.count('\n')
print thefile2,"has" , countFile2, "function calls"
file2N.close()


print 
print 
print


# analyze the android.app function


#generate a new file contains word about the key
#three variable: file1 , file2 ,  


def generatingFilefor(text_word , theComparsionfile1, theComparsionfile2, newOpenFile1, newOpenFile2, therealDifference):

	file_object1_2 = open(newOpenFile1, 'w')
	file_object2_2 = open(newOpenFile2, 'w')

	numberOfStyle1 = 0;
	file1 = open(theComparsionfile1).readlines();
	for line in file1:
		if text_word in line:
			numberOfStyle1= numberOfStyle1+1
			#remove the text_word
			line = re.sub(text_word,'',line)
			file_object1_2.write(line)

	print theComparsionfile1, " contain functions started with" + str(text_word) + " s number is " + str(numberOfStyle1)
	file_object1_2.close();



	numberOfStyle2 = 0;
	file2 = open(theComparsionfile2).readlines();
	for line2 in file2:
		if text_word in line2:
			numberOfStyle2 = numberOfStyle2+1
			line2 = re.sub(text_word,'',line2)
			file_object2_2.write(line2)
	print theComparsionfile2, " contain functions with with android.app number is", numberOfStyle2
	file_object2_2.close();

	print 
	print


	theDifference = open(therealDifference, 'w')
	
	#try another approach
	#render line by line
	with open(newOpenFile1) as f:
	    t1 = f.readlines()

	for Oline1 in t1:
		if Oline1 in open(newOpenFile2).readlines():
			continue
		else:
			theDifference.write(Oline1)



	with open(newOpenFile2) as f:
	    t2 = f.readlines()

	for Oline2 in t2:
		if Oline1 in open(newOpenFile1).readlines():
			continue
		else:
			theDifference.writelines(Oline2)









#the first variable would be the key word
#thefile1 would be the original files name
#thefile2 would be the original files name -2
#the rest would be the file you want to gnerate

#for android.R$styleable
generatingFilefor('android.R$styleable.', thefile1, thefile2, 'file1-android.R$styleable.txt', 'file2-android.R$styleable.txt', "diffinR$styleable.txt" )

# #for android.app
generatingFilefor('android.app.', thefile1, thefile2, 'file1-android.app.txt', 'file2-android.app.txt', "diffinapp.txt")

#for android.content
generatingFilefor('android.content.', thefile1, thefile2, 'file1-android.content.txt', 'file2-android.content.txt','diffcontent.txt')

#forandroid.database
generatingFilefor('android.database.', thefile1, thefile2, 'file1-android.database.txt', 'file2-android.database.txt','diffdatabase.txt')

#for android.ddm
generatingFilefor('android.ddm.', thefile1, thefile2, 'file1-android.ddm.txt', 'file2-android.ddm.txt',"diffddm.txt")

#for android graphics
generatingFilefor('android.graphics.', thefile1, thefile2, 'file1-android.graphics.txt', 'file2-android.graphics.txt', 'diffgraphics.txt')

#for android.hardware
generatingFilefor('android.hardware.', thefile1, thefile2, 'file1-android.hardware.txt', 'file2-android.hardware.txt', 'diffhardware.txt')

#for android.location
generatingFilefor('android.location.', thefile1, thefile2, 'file1-android.location.txt', 'file2-android.location.txt', 'difflocation.txt')

#for android.media
generatingFilefor('android.media.', thefile1, thefile2, 'file1-android.media.txt', 'file2-android.media.txt','diffmedia.txt')

#for android.net
generatingFilefor('android.net.', thefile1, thefile2, 'file1-android.net.txt', 'file2-android.net.txt','diffnet.txt')

#for android.nfc
generatingFilefor('android.nfc.', thefile1, thefile2, 'file1-android.nfc.txt', 'file2-android.nfc.txt','diffnfc.txt')

#for android.opengl
generatingFilefor('android.opengl.', thefile1, thefile2, 'file1-android.opengl.txt', 'file2-android.opengl.txt','diffopengl.txt')

#for android.os
generatingFilefor('android.os.', thefile1, thefile2, 'file1-android.os.txt', 'file2-android.os.txt','diffos.txt')

#for android.provider
generatingFilefor('android.provider.', thefile1, thefile2, 'file1-android.provider.txt', 'file2-android.provider.txt','diffprovider.txt')

#for android.text
generatingFilefor('android.text.', thefile1, thefile2, 'file1-android.text.txt', 'file2-android.text.txt','diffandroid.txt')

#for android.util
generatingFilefor('android.util.', thefile1, thefile2, 'file1-android.util.txt', 'file2-android.util.txt','diffutil.txt')

#for android.view
generatingFilefor('android.view.', thefile1, thefile2, 'file1-android.view.txt', 'file2-android.view.txt','diffview.txt')

#for android.widget
generatingFilefor('android.widget.', thefile1, thefile2, 'file1-android.widget.txt', 'file2-android.widget.txt', 'diffwidget.txt')

#for com.android.internal
generatingFilefor('com.android.internal.', thefile1, thefile2, 'file1-com.android.internal.txt', 'file2-com.android.internal.txt','diffinternal.txt')

#for com.android.org
generatingFilefor('com.android.org.', thefile1, thefile2, 'file1-com.android.org.txt', 'file2-com.android.org.txt','difforg.txt')

#for com.android.webview
generatingFilefor('com.android.webview.', thefile1, thefile2, 'file1-com.android.webview.txt', 'file2-com.android.webview.txt','diffwebview.txt')

















