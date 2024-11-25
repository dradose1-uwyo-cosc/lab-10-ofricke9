# Oliver Fricke
# UWYO COSC 1010
# 11-21-24
# Lab 10
# Lab Section: 13
# Sources, people worked with, help given to: Help GIVEN TO - Cody Phillips (roommate)
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()

# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-else block in your code.
# - The reading of files needs to occur in the try blocks.

p = Path('hash')
dec = Path('rockyou.txt')

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

try:
    crack = p.read_text().strip()
except FileNotFoundError:
    print("Error")

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.

try:
    password = dec.read_text().splitlines()
except FileNotFoundError:
    print("Error")

try:
    for line in password:
        if get_hash(line) == crack:
            print(f"The name of the password is: {line}")
            print(f"The 256-bit of the password is: {crack}")
except ValueError:
    print("Error")