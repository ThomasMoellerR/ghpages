import subprocess
import time

def file_to_string(path, mode = "r"):
	s = ""
	file = open(path, mode)
	s = file.read()
	file.close()
	return s

def string_to_file(path, s, mode = "w"):
    file = open(path, mode)
    file.write(s)
    file.close()

while True:
	time.sleep(1)
	
	if file_to_string("update.txt") == "update":
	
		result = subprocess.run(['sh', 'git.sh'], stdout=subprocess.PIPE)
		a = result.stdout

		print(a)

		string_to_file("update.txt" "")

		print("uploaded files to github pages")
	else:
		print("nothing to do")