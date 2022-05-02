import secrets, random
from datetime import datetime


def TRNG():
    # generates a random number based on operating system state (physical entropy)
    # acts like TRNG
    time = datetime.now()  # different variable depending on the day
    entropy = secrets.SystemRandom(time.microsecond)  # secrets library used in cryptography compared to random library
    float = entropy.uniform(6.9, 25601.420)
    print("The \"TRNG\" value is: ", float)
    PRNG(float)


def PRNG(float):
    # attempting to combine TRNG physical entropy with PRNG
    seed = round((float * ((random.randint(1, random.randint(420, 6969))))))
    print("The PRNG value is: ", seed)
    print("The value of FU is: ", bitstream(seed))


# idea is sort of based of a pseudorandom binary sequence
# without entropy or seed, this function is deterministic
def bitstream(U_is_for_uNmeee):
    for i in range(16):
        # I was trying to make this process complicated for a good "random" number
        # sort of monic polynomial-ish
        # inverts bit shifted num, AND XORing bitshifted num
        F_is_for_friends = ~((U_is_for_uNmeee >> 12) ^ (U_is_for_uNmeee >> 25)) & 0x01
        # logically determines larger bit shifted value
        U_is_for_uNmeee = ((U_is_for_uNmeee << 2) | F_is_for_friends) & 0xFFFFFFFF
    return U_is_for_uNmeee


def main():
    print("Best of luck trying to predict this number")
    print("I call it the FU algorithm :)\n")
    TRNG()


if __name__ == "__main__":
    main()

