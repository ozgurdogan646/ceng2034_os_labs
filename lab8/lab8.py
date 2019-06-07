import os
import binascii

currentdir = os.getcwd()
filelist=os.listdir(currentdir + "/files")
currentFolders = os.listdir(currentdir)


for myfile in filelist :
	with open(filename, 'rb') as f:
    	content = f.read()


	hexString = binascii.hexlify(content)


	magic_N = "00"


	for chars in hexString:
		newFile = ""
    	if chars == magic_N:
        	newFile += chars.len(9)


    	if newFile != "":
        	i = 0
        	while os.path.exists("output_file%s.xyz" % i):
          	i += 1
        	fh = with open("output_file%s.xyz" % i, "wb"):
            		newFile
	if magic_N=="FF D8":
    		if "jpgFolder" not in currentFolders:
      			os.mkdir("jpgFolder")
      			currentFolders=os.listdir(currentDir)
    			os.system("cp "+currentDir+"/files/"+takeFile+" jpgFolder")

  	if magic_N=="89 50":
    		if "pngFolder" not in currentFolders:
      			os.mkdir("pngFolder")
      			currentFolders=os.listdir(currentDir)
    			os.system("cp "+currentDir+"/files/"+takeFile+" pngFolder")

  	if magic_Nr=="78 79":
    		if "txtFolder" not in currentFolders:
      			os.mkdir("txtFolder")
      			currentFolders=os.listdir(currentDir)
    			os.system("cp "+currentDir+"/files/"+takeFile+" txtFolder")

  	if magic_N=="49 44":
    		if "mp3Folder" not in currentFolders:
      			os.mkdir("mp3Folder")
      			currentFolders=os.listdir(currentDir)
			os.system("cp "+currentDir+"/files/"+takeFile+" mp3Folder")
