#m22ai608
#Task 1: Universal Hash Functions

import sys

def hash_function_1(s):
    hash_val = 0
    prime = 31
    for char in s:
        hash_val = (hash_val * prime + ord(char)) % 64
    return hash_val % 64

def hash_function_2(s):
    hash_val = 0
    prime = 37
    for char in s:
        hash_val = (hash_val * prime + ord(char)) % 64
    return hash_val % 64

def hash_function_3(s):
    hash_val = 0
    prime = 41
    for char in s:
        hash_val = (hash_val * prime + ord(char)) % 64
    return hash_val % 64

def hash_function_4(s):
    hash_val = 0
    prime = 43
    for char in s:
        hash_val = (hash_val * prime + ord(char)) % 64
    return hash_val % 64

def hash_function_5(s):
    hash_val = 0
    prime = 47
    for char in s:
        hash_val = (hash_val * prime + ord(char)) % 64
    return hash_val % 64

def aggregate_hash_functions(s):
    hashes = [
        hash_function_1(s),
        hash_function_2(s),
        hash_function_3(s),
        hash_function_4(s),
        hash_function_5(s)
    ]
    return hashes

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python hashing.py <input_string>")
    else:
        input_string = sys.argv[1]
        hashes = aggregate_hash_functions(input_string)
        print(','.join(str(hash_val) for hash_val in hashes))

# =============================================================================
# Output : python hashing.py algorithm
# 47,55,39,47,47
# =============================================================================
