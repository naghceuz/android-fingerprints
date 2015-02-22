
This is a python script which will generate a analysis report based on the input of two files.


To Run the script:

Move the two files with the txt format that you want to do comparsion into the same directory as this python script in your computer. 

python file1.txt file2.txt

It will generate different files based and generate a comprehensive report of the difference between file1.txt and file2.txt.



The value of this script:
The Standard Android emulator fingerprint code(from Android Developer Official Websitde) has more than 1,5000 lines of java code. Each line is a function of different purpose. For cell phone companies uses Android platoform, they will first download the standard Android emulator source code and will modification based on the Android emulator source code. Finally the fingerprint in your Android device is just the modification of the Android emulator source code.

According to life observation and academic paper(CMU + Morephes), the malware writers do try to call some functions to testify if the App with virus are in an emulator environment or in read device. 

Therefore, the emulator's using to test malware should look like emulator as much as possible.

This script will analysis the andriod fingerprint and point out what is the difference between device and emulators or other devices.

So , if you are an Android malware writers, this script can help you to figure out what is some functions that your target Android device will have but the general Android emulator will not have; then you can try to call those functions to figure out if you are in Android emlator or not.


If you are in the defensive side, you can use this script to improve your emulator:adding these missing function and making it like a real device. Then you are able to find out the malware and report to the public.



