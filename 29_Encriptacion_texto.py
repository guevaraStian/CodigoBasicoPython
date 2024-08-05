
import hashlib

def main():
    palabra = str(input("Ingrese la palabra a encriptar: "))

    md5 = hashlib.md5(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash MD5: " + md5)

    sha1 = hashlib.sha1(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha1: " + sha1)

    sha224 = hashlib.sha224(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha224: " + sha224)

    sha256 = hashlib.sha256(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha256: " + sha256)

    sha384 = hashlib.sha384(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha384: "+ sha384)

    sha512 = hashlib.sha512(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha512: "+ sha512)

if __name__== "__main__":
    main()





