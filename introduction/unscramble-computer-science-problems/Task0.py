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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# Get the first record from texts
first_text = texts[0]  
sending, receiving, time = first_text
print(f"First record of texts, {sending} texts {receiving} at time {time}")

# Get the last record from calls
last_call = calls[-1]  
caller, receiver, time, duration = last_call
print(f"Last record of calls, {caller} calls {receiver} at time {time}, lasting {duration} seconds")
