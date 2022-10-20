import hashlib

hash_value='eba78765396a7b1aa00a24fd92e1a2a64b1012e5'
def sha1(filename):
    BUF_SIZE = 65536  # read stuff in 64kb chunks!
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()
    
    

original_file = 'H:/github/File_integrity_Monitoring/original_file.txt'
original_file_hash = sha1(original_file)

file_copy = 'H:/github/File_integrity_Monitoring/file_copy.txt'
file_copy_hash = sha1(file_copy)


#print ("the hash of the file is \n",file_hash)

if original_file_hash == file_copy_hash:
	print("the origanal and the copy file are the same")

else:
	print("the content in the copy file changed")
	
