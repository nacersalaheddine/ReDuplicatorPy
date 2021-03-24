import hashlib

def available_hashes():
	print(hashlib.algorithms_available)

def sha1_hash_func(file_name):
	sha1 = hashlib.sha1()
	with open(file_name,"rb") as file:
		data = file.read()
		sha1.update(data)
	return sha1.hexdigest()



'''
print("MD5: {0}".format(md5.hexdigest()))
print("SHA1: {0}".format(sha1.hexdigest()))
'''