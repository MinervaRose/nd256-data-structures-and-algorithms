"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# Dictionary to hold phone number -> total time
call_durations = {}

# Go through each call record
for call in calls:
    caller, receiver, _, duration = call
    duration = int(duration)  # Convert duration to integer

    # Add duration to caller
    if caller in call_durations:
        call_durations[caller] += duration
    else:
        call_durations[caller] = duration

    # Add duration to receiver
    if receiver in call_durations:
        call_durations[receiver] += duration
    else:
        call_durations[receiver] = duration

# Find the number with the longest time
max_number = max(call_durations, key=call_durations.get)
max_time = call_durations[max_number]

# Print the result
print(f"{max_number} spent the longest time, {max_time} seconds, on the phone during September 2016.")

