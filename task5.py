#m22ai608
#Task 5: Measuring False Positive Rate

import os
import csv
from pybloom_live import BloomFilter

def calculate_false_positive_rate(bloom_filter, negative_queries):
    false_positives = 0
    total_queries = len(negative_queries)

    for query in negative_queries:
        if query in bloom_filter:
            false_positives += 1

    false_positive_rate = false_positives / total_queries
    return false_positive_rate

# Define the path to the DATA folder and testing queries CSV file
data_folder = r"C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task5\DATA"  # Replace with the actual path to the DATA folder
testing_queries_file = r"C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task5\testing_queries.csv"  # Replace with the actual path to the testing queries CSV file

# Load the testing queries
negative_queries = []
with open(testing_queries_file, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        negative_queries.append(row[0])

# Calculate false positive rate for each filter
false_positive_rates = []
accuracies = []
for i in range(32):
    bloom_filter = BloomFilter(capacity=10000, error_rate=0.001)  # Increase capacity to accommodate more elements

    # Generate the Bloom filter for each file in the DATA folder
    for filename in os.listdir(data_folder):
        file_path = os.path.join(data_folder, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                keywords = line.strip().split(',')
                for keyword in keywords:
                    bloom_filter.add(keyword)

    false_positive_rate = calculate_false_positive_rate(bloom_filter, negative_queries)
    false_positive_rates.append(false_positive_rate)
    accuracy = 1 - false_positive_rate
    accuracies.append(accuracy)

# Write false positive rates and accuracies to a text file
output_file_path = r"C:\Users\Admin\OneDrive\Desktop\bigdata-assign2-m22ai608\task5\false_positive.txt"  # Replace with the desired output file path
with open(output_file_path, 'w', encoding='utf-8') as file:
    for i in range(32):
        file.write(f"Filter {i+1} - False Positive Rate: {false_positive_rates[i]}, Accuracy: {accuracies[i]}\n")


# =============================================================================
# output: it will generate false_positive.txt file 
# Filter 1 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 2 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 3 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 4 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 5 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 6 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 7 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 8 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 9 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 10 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 11 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 12 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 13 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 14 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 15 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 16 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 17 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 18 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 19 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 20 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 21 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 22 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 23 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 24 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 25 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 26 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 27 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 28 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 29 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 30 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 31 - False Positive Rate: 0.0, Accuracy: 1.0
# Filter 32 - False Positive Rate: 0.0, Accuracy: 1.0
# 
# =============================================================================
