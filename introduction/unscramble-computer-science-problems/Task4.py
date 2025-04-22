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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# All numbers that make outgoing calls
callers = set(call[0] for call in calls)

# Numbers that receive calls, send texts, or receive texts
non_telemarketers = set()

# Add receivers of calls
for call in calls:
    non_telemarketers.add(call[1])

# Add both senders and receivers of texts
for text in texts:
    non_telemarketers.add(text[0])
    non_telemarketers.add(text[1])

# Step 3: Telemarketers = callers - non_telemarketers
telemarketers = callers - non_telemarketers

# Sort and print
print("These numbers could be telemarketers:")
for number in sorted(telemarketers):
    print(number)
