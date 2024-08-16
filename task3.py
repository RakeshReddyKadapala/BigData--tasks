#m22ai608
#Task 3: Bloom Filter Creation

import os
import hashlib
from bitarray import bitarray

# Function to generate multiple hash functions
def generate_hash_functions(keyword):
    hash_values = []
    sha256_hash = hashlib.sha256(keyword.encode()).digest()
    md5_hash = hashlib.md5(keyword.encode()).digest()

    for i in range(64):
        combined_hash = int.from_bytes(sha256_hash, 'big') + int.from_bytes(md5_hash, 'big') + i
        hash_value = hashlib.sha256(combined_hash.to_bytes(32, 'big')).hexdigest()
        bit_position = int(hash_value, 16) % 64
        hash_values.append(bit_position)

    return hash_values

# Function to generate a Bloom filter from a list of keywords
def generate_bloom_filter(keywords):
    bloom_filter = bitarray(64)
    bloom_filter.setall(0)

    for keyword in keywords:
        hash_values = generate_hash_functions(keyword)
        for bit_position in hash_values:
            bloom_filter[bit_position] = 1

    return bloom_filter.to01()

# Set the paths for the keywords folder and filters folder
keywords_folder = 'C:\\Users\\Admin\\OneDrive\\Desktop\\bigdata-assign2-m22ai608\\task3\\Keywords'
filters_folder = 'C:\\Users\\Admin\\OneDrive\\Desktop\\bigdata-assign2-m22ai608\\task3\\Filters'

# Create the filters folder if it doesn't exist
os.makedirs(filters_folder, exist_ok=True)

# Iterate over the keyword files in the keywords folder
for filename in os.listdir(keywords_folder):
    # Get the full path of the keyword file
    keyword_file = os.path.join(keywords_folder, filename)

    # Read the keywords from the file
    with open(keyword_file, 'r') as file:
        keywords = file.read().splitlines()

    # Generate the Bloom filter for the keywords
    bloom_filter = generate_bloom_filter(keywords)

    # Create the filter file path in the filters folder
    filter_file = os.path.join(filters_folder, os.path.splitext(filename)[0] + '.txt')

    # Write the Bloom filter to the filter file
    with open(filter_file, 'w') as file:
        file.write(bloom_filter)


# =============================================================================
# output: generates Filters folder
# here in 12.txt i got ouput as 1111111000011111111111011111000110010110111111110010010101010010 
# like this in folder it will generate 0's and 1's
# =============================================================================
