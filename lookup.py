#m22ai608
#Task 4: Lookup Mechanism

########## Searching for the given word among all in all the keyword files and prints the file names where given word presents

import sys
import os

def lookup(keyword):
    keyword = keyword.lower()  # Convert the keyword to lowercase for case-insensitive comparison

    # Define the path to the folder containing the keyword files
    folder_path = r"C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task4\Keywords"

    file_list = os.listdir(folder_path)  # Get the list of files in the folder

    present_files = []

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):  # Check if the file exists
            with open(file_path, 'r') as file:
                content = file.read().lower()  # Read the file content and convert it to lowercase

                if keyword in content:
                    present_files.append(file_name)

    return present_files

# Get the keyword from the command line argument
keyword = sys.argv[1] if len(sys.argv) > 1 else ""

# Perform the lookup and print the result
result = lookup(keyword)

if result:
    print(f"The word '{keyword}' is present in the following files:")
    for file_name in result:
        print(file_name)
else:
    print(f"The word '{keyword}' is not present in any file.")


# Code for Binary format: it counts how many times where given word presents in total files
import sys
import os
import re

def lookup(keyword):
    keyword = keyword.lower()  # Convert the keyword to lowercase for case-insensitive comparison

    # Define the path to the folder containing the keyword files
    folder_path = r"C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task4\Keywords"

    result = []  # Initialize an empty result list

    file_list = os.listdir(folder_path)  # Get the list of files in the folder

    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)

        if os.path.isfile(file_path):  # Check if the file exists
            with open(file_path, 'r') as file:
                content = file.read().lower()  # Read the file content and convert it to lowercase

                if keyword in content:
                    file_number = re.search(r'\d+', file_name)  # Extract the numeric part from the file name using regex
                    if file_number:
                        file_number = int(file_number.group())  # Convert the extracted part to an integer

                        # Resize the result array if needed
                        while len(result) < file_number:
                            result.append(False)

                        result[file_number - 1] = True  # Set the corresponding result value to 'True' if the keyword is possibly present

    # Fill the remaining file numbers with False values
    while len(result) < 32:
        result.append(False)

    return result

# Get the keyword from the command line argument
keyword = sys.argv[1] if len(sys.argv) > 1 else ""

# Perform the lookup and print the result
result = lookup(keyword)
result_string = ''.join(['1' if val else '0' for val in result])
print(f"The Binary Format '{result_string}' ")


# =============================================================================
# output: The word 'microsoft' is present in the following files:
# 13.txt
# 28.txt
# 78.txt
# 82.txt
# The Binary Format '0000000000001000000000000001000000000000000000000000000000000000000000000000010001'
# 
# The word 'protection' is present in the following files:
# 43.txt
# The Binary Format '0000000000000000000000000000000000000000001'
# 
# The word 'rakesh' is not present in any file.
# The Binary Format '00000000000000000000000000000000'
# =============================================================================
