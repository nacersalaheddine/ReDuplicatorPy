from hash_util import sha1_hash_func
import os

extensions = [".png",".jpg",".jpeg",".gif"]
path = "./"
duplicates_dir = "./المدوبلين"
files_dict = {}


files = os.listdir(path)
filtered_files = list(filter(lambda f:os.path.splitext(f)[1].lower() in extensions,files))
#print([f for f in files if f.endswith(extension)])

if(not os.path.exists(duplicates_dir)):
	os.mkdir(duplicates_dir)

for file_name in filtered_files:
	hash_hex = sha1_hash_func(file_name)
	if not hash_hex in files_dict:
		files_dict[hash_hex] = file_name
	else:
		#move repeated file
		print("move",file_name)
		os.replace(file_name,'./'+duplicates_dir+'/'+file_name)
		


