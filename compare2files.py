import hashlib
# import file1.txt
def fileComp(file1,file2):
    h1=hashlib.md5()
    h2=hashlib.md5()

    with open(file1,'rb') as data:
        chunk=0
        while chunk != b'':
            chunk=data.read(65536)
            h1.update(chunk)
    with open(file2,'rb') as data:
        chunk=0
        while chunk != b'':
            chunk=data.read(65536)
            h2.update(chunk)
    return h1.hexdigest(),h2.hexdigest()

f1,f2=fileComp("miniprojects/file3.txt","miniprojects/file1.txt")

if f1==f2:
    print("these files are identical.")
else:
    print("these files are different.")    
