from zipfile import ZipFile
from cryptocode import encrypt,decrypt

class spw:
    
    def auth(obj,mode):
        with ZipFile('./sec/mpwd.zip') as zf:
            if mode == 'set':
                return(encrypt(obj,password=zf.open('mpwd.txt',pwd=b'mbadmin').readline().decode('utf-8')))
            elif mode == 'get':
                return(decrypt(obj,password=zf.open('mpwd.txt',pwd=b'mbadmin').readline().decode('utf-8')))