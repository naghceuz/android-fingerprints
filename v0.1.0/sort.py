try:
	f = open("Google-emulator.txt", "r")

	try:
		lines = f.readlines()
		lines.sort()
		f.close()
		f = open("Google-New-emulator.txt","w");
		f.writelines(lines)
	finally:
		f.close()
except IOError:
	pass
