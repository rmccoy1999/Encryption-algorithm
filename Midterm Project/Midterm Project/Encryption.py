
# need pip3 install pycrypto or pip3 install pycryptodomex
import hashlib
import os
from base64 import b64encode, b64decode
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

#def breakfastHash(egg): #used for testing, might use it in future for hash
    #bacon = hashlib.sha3_256(egg.encode('utf-8')).hexdigest()
    #print(bacon)
#breakfastHash("I Love You")


def LetsEncryptSomeShit(message, key): #encrypts the shit of message
    happiness_or_raised_bloodsugar = get_random_bytes(AES.block_size) #computes the salt
    #using the key and scrypt kdf, creates private key
    private_key = hashlib.scrypt(key.encode(), salt=happiness_or_raised_bloodsugar, n=2**14, r=8, p=1, dklen=32)
    mathShit = AES.new(private_key, AES.MODE_GCM) #creates galois framework. IV and private key result XORed with message

    cipher_framework, tag = mathShit.encrypt_and_digest(bytes(message, 'utf-8')) #converts to immuntable object cipher can't change
    encrypt_values = { #dictionary for decrypt reference later
        "cipher": b64encode(cipher_framework).decode('utf-8'), #converts message into ascii characters
        "sprinkleOsalt": b64encode(happiness_or_raised_bloodsugar).decode('utf-8'),
        "randoNonce": b64encode(mathShit.nonce).decode('utf-8'),
        "tag": b64encode(tag).decode('utf-8')
    }
    return encrypt_values
    

def LetsDecryptSomeShit(encrypt_values, key): #decrypts the shit of message
    #retrieves and decodes values from dictionary, back into original utf-8 values
    cipher = b64decode(encrypt_values['cipher']) 
    salt = b64decode(encrypt_values['sprinkleOsalt'])
    nonce = b64decode(encrypt_values['randoNonce'])
    tag = b64decode(encrypt_values['tag'])
    
    private_key = hashlib.scrypt(key.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32) #creates private key from password and salt
    cipher_framework = AES.new(private_key, AES.MODE_GCM, nonce=nonce) #creates decrypt framework with previous values
    decrypt_values = cipher_framework.decrypt_and_verify(cipher, tag) #well, decrypts the values, apart of cryptodome as hash

    return decrypt_values


