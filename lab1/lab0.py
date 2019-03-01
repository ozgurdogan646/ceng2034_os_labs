import os 
import os.path , time
os.chdir("/home")
os.mkdir("os_lab_0")
os.chdir("/home/os_lab_0")
open("first.txt","w")
open("second.txt" , "w")
open("third.py" , "w")
print("Last modified of first.txt : %s" % time.ctime(os.path.getmtime("first.txt")))
print("Last modified of second.txt : %s" % time.ctime(os.path.getmtime("second.txt")))
print("Last modified of third.py : %s" % time.ctime(os.path.getmtime("third.py")))
for file in os.listdir("/home/os_lab_0") :
	if file.endswith(".txt"):
		print(os.path.join("/home" , file ))
