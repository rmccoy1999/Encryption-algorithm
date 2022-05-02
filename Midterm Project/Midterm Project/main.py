#The encryption and description algorithm requires:
#   Input and output of a 16 Character (8bit) String
#   Security Key of 32 bytes
#   Use two round functions which contain
#       Substitution 
#       Permutation
#       Diffusion
#       Confusion
#       Key Schedule
#       Padding


import random, string
from  SBox import encoding


def wittleFireTruckThatCould(secret_msg):
    #fix in future; remove padding on decrypted message, not a massive deal
    
    for i in range(10-len(secret_msg)): #finds remainder of length, and picks pseudorandom ascii letters
        secret_msg += random.choice(string.ascii_letters) #concats padding to secret_msg
    print("\nToo short, add padding. Its how you use it ;)")
    print("New string is: ", secret_msg)
    return secret_msg


def chungus(secret_msg, key):
    
    #loops through and parses length of 10 characters, storing in glblits
    giblits = [secret_msg[i:i+10] for i in range(0, len(secret_msg), 10)] 
    print("New strings are: ", giblits, "\n")
    print("------------------------------------------------------------------") 
    for index, taco in enumerate(giblits): 
        if len(taco) == 10: #if result is 10, start encrypting
            encoding(taco, key)
        else:
            print() #calls for add padding to shorter part of message
            encoding(wittleFireTruckThatCould(taco), key)



def main():
    secret_msg = "I Love You"
    key = 69568420
    option = 0
    
    
    if len(secret_msg) < 10: #going to call wittleFireTruckThatCould()
        print("Too short, add padding. Its how you use it ;)")
        encoding(wittleFireTruckThatCould(secret_msg), key)
        
    elif len(secret_msg) > 10: #going to call chungus() method to cut string in junks
        #for the sake of your computer, not truly needed though
        if len(secret_msg) > 30: 
            print("C'mon maannn, you know, the thing...\nShorter message.") #good ol joey
        else:
            print("Too long...nice. Time to de-girth ;)")
            chungus(secret_msg, key)
           
    else: #if secret_msg is already 10 characters long
        print("String is good bruh\nYour string is: ", secret_msg)
        print("------------------------------------------------------------------") 
        encoding(secret_msg, key)



if __name__ == "__main__":
    main()