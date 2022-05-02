import numpy as math
import hashlib, uuid
from Encryption import LetsEncryptSomeShit, LetsDecryptSomeShit


def reverse_expansion(expanded_array, key, r3):
    unreversed = []
    for index, exp in enumerate(expanded_array): #for reversing expansion
        unreversed.append(round((exp^r3)/key)) #reverses computed value of exp*key^r3
    return(unreversed)

def key_expansion(permuted, key, round): #for lengthening the permuted values
    
    k1 = str(key)[2:4]+str(key)[0:2] #another way of mixing/flipping two-pair values, for new key
    k2 = str(key)[6:8]+str(key)[4:6] #saves

    r1 = int(str(key)[:4])<<1 #takes flipped values of key, and bit shifts them
    r2 = int(str(key)[4:])<<1

    r3 = r1>>2 #shifts entire value over two
    r4 = r2>>2
    
    expanded = []
    for index, exp in enumerate(permuted): #for actual expansion of values
        expanded.append(exp*key^r3) #simply math logic for expanded value, can be more complicated if needed
    print("Expanded key values: ", expanded)
    length = [] #needed because some of the expanded values computed are over 11 digits while others are 10, screws up decoding
    for index, element in enumerate(expanded):
        length.append(len(str(expanded[index]))) #stores length of each expanded value in length array
    print("Length array is: ", length)
    
    
    #combines mixed, computed, and expanded values into one value for easy encryption
    combined = str((''.join(map(str, expanded)))) #so encrypt_msg call is one value instead of 10
    unlock = str(key) #unlock key that is used to encrypt, and decrypt message
    print("Combined Expanded: ", combined)


    encrypt_msg = LetsEncryptSomeShit(combined, unlock) #calls encrypt message to well, encrypt
    print("The end encrypted message is: \n", encrypt_msg) 
    print("---------------------------------")
    #returns decoded string from the given bytes, cast as string variable
    decrypt_msg = str(bytes.decode(LetsDecryptSomeShit(encrypt_msg, unlock))) #takes unlock key and encrypted message, for decoding
    print("The decrypted message is: ", decrypt_msg)
    
    giblits = [] #store decrypted values at original length
    counter=0
    for index, element in enumerate(length): #this impinged my soul and brain after the 10 hours of working
        giblits.append(decrypt_msg[counter:(counter+element)]) #uses saved element values,                   
        counter+=(element) #and parses large decrypted value into their original, respecting their original lengths
    print("Giblits: ", giblits)
    
    print("Un-expanded values: ", reverse_expansion(expanded, key, r3))
    return reverse_expansion(expanded, key, r3)

