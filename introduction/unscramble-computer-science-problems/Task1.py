"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Create a set to store unique numbers
unique_numbers = set()

# Add numbers from texts
for text in texts:
    sending_number, receiving_number, _ = text
    unique_numbers.add(sending_number)
    unique_numbers.add(receiving_number)

# Add numbers from calls
for call in calls:
    calling_number, receiving_number, _, _ = call
    unique_numbers.add(calling_number)
    unique_numbers.add(receiving_number)

# Print the result
print(f"There are {len(unique_numbers)} different telephone numbers in the records.")
