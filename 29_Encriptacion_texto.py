
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

    #Añadidos desde python 3.6 en adelante
    blake2b = hashlib.blake2b(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash blake2b: "+ blake2b)

    blake2s = hashlib.blake2s(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash blake2s: "+ blake2s)

    sha3_224 = hashlib.sha3_224(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_224: "+ sha3_224)

    sha3_256 = hashlib.sha3_256(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_256: "+ sha3_256)

    sha3_384 = hashlib.sha3_384(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_384: "+ sha3_384)

    sha3_512 = hashlib.sha3_512(palabra.encode('utf-8')).hexdigest()
    print("Este es el hash sha3_512: "+ sha3_512)

    #sha3 = hashlib.sha3(palabra.encode('utf-8')).hexdigest()
    #print("Este es el hash sha3: "+ sha3)

    #shake_128 = hashlib.shake_128(palabra.encode('utf-8')).hexdigest()
    #print("Este es el hash shake_128: "+ shake_128)

    #shake_256 = hashlib.shake_256(palabra.encode('utf-8')).hexdigest()
    #print("Este es el hash shake_256: "+ shake_256)





    

if __name__== "__main__":
    main()





