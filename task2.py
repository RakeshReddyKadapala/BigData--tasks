#m22ai608
#Task 2: Keywords Extraction

import os
import csv
import re
from collections import Counter

# Function to extract keywords from a text file
def extract_keywords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Remove non-alphanumeric characters and convert to lowercase
        clean_text = re.sub(r'\W+', ' ', text).lower()
        # Split the text into individual words
        words = clean_text.split()
        # Count the frequency of each word
        word_count = Counter(words)
        # Filter out words with frequency greater than or equal to 2
        keywords = [word for word, count in word_count.items() if count >= 2]
        # Join the keywords with commas
        keywords_str = ', '.join(keywords)
        return keywords_str

# Create the Keywords folder if it doesn't exist
keywords_folder = 'C:\\Users\\Admin\\OneDrive\\Desktop\\bigdata-assign2-m22ai608\\task2\\keywords'
os.makedirs(keywords_folder, exist_ok=True)

# Read the assigned file numbers from the CSV file
csv_file = 'C:\\Users\\Admin\\OneDrive\\Desktop\\bigdata-assign2-m22ai608\\task2\\assigned_files.csv'
assigned_files = []
counter = 0
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # skip header
    for row in csv_reader:
        roll_number = row[0]
        # roll num finding in assigned files
        if roll_number == 'M22AI608':
            assigned_files = row[2:]
            print(assigned_files)
            print(len(assigned_files))

    # Process the assigned files
    for file_num in assigned_files:
        file_num = file_num + '.txt'
        file_path = os.path.join('C:\\Users\\Admin\\OneDrive\\Desktop\\bigdata-assign2-m22ai608\\task2\\DATA', file_num)  # Replace with the actual path to the directory containing the text files
        print(file_path)
        output_file_path = os.path.join(keywords_folder, file_num)  # Replace 'Keywords' with your desired output folder name
        keywords = extract_keywords(file_path)
        print(len(keywords))

        # write keywords to output file
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(keywords)


# =============================================================================
# output:
#     ['1', '12', '13', '18', '21', '22', '23', '26', '27', '28', '31', '33', '34', '37', '43', '44', '46', '48', '64', '69', '70', '71', '72', '76', '78', '81', '82', '87', '88', '89', '91', '97']
#     32
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\1.txt
#     630
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\12.txt
#     269
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\13.txt
#     540
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\18.txt
#     418
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\21.txt
#     118
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\22.txt
#     346
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\23.txt
#     475
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\26.txt
#     528
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\27.txt
#     515
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\28.txt
#     351
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\31.txt
#     843
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\33.txt
#     361
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\34.txt
#     698
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\37.txt
#     235
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\43.txt
#     387
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\44.txt
#     296
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\46.txt
#     355
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\48.txt
#     102
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\64.txt
#     758
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\69.txt
#     675
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\70.txt
#     138
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\71.txt
#     388
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\72.txt
#     980
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\76.txt
#     405
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\78.txt
#     838
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\81.txt
#     562
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\82.txt
#     539
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\87.txt
#     582
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\88.txt
#     516
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\89.txt
#     381
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\91.txt
#     339
#     C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task2\DATA\97.txt
#     505
# 
# =============================================================================
