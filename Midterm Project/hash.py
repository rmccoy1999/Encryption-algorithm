
#not used at this point, was goingt to use it for checksum
def hash_function(input_value):
    tadOsalt = uuid.uuid4().hex # uuid is used to generate a random number
    return hashlib.sha256(tadOsalt.encode()+input_value.encode()).hexdigest()+':'+ tadOsalt
    
def hash_check(breakfast_hash, combined):
    hash, tadOsalt = breakfast_hash.split(':')
    return hashlib.sha256(tadOsalt.encode()+combined.encode()).hexdigest()
    #return hash == hashlib.sha256(tadOsalt.encode() + combined.encode()).hexdigest() #for returning true or false, compare

def hash(permuted, key, round):
    combined = (''.join(map(str, permuted)))
    print(combined)

    breakfast_hash = hash_function(combined)
    print("Hashed value is    : ", breakfast_hash)
    print("Hash check value is: ", hash_check(breakfast_hash, combined))