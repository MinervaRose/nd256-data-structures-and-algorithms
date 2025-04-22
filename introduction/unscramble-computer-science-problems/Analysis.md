## Task0

**Description**: Find the first record of texts and the last record of calls.

**Approach**: 
- Read both files into lists.
- Access `texts[0]` for the first text and `calls[-1]` for the last call.
- Print the relevant fields from each.

**Complexity Analysis**:
- **Reading CSV files**: O(n + m) where n is number of texts and m is number of calls.
- **Accessing list items**: O(1)
- **Overall Time Complexity**: O(n + m)
- **Justification**: The dominant cost is reading the data into memory. Accessing specific rows is constant time.


## Task1

**Description**: Count how many **unique telephone numbers** appear in both text and call records.

**Approach**:
- Loop through each row in both `texts` and `calls`.
- Add each number to a set (which handles duplicates automatically).
- Return the length of the set.

**Complexity Analysis**:
- **Looping through texts and calls**: O(n + m)
- **Set insertion**: O(1) average time per number
- **Overall Time Complexity**: O(n + m)
- **Justification**: Each number is processed once and added to a set, which is efficient.


## Task2

**Description**: Find the telephone number that spent the **longest total time** on the phone.

**Approach**:
- Loop through each call record.
- Add the duration to both the caller's and receiver's total in a dictionary.
- Use `max()` to find the number with the highest total.

**Complexity Analysis**:
- **Looping through calls**: O(m)
- **Dictionary insertion/update**: O(1) average per operation
- **Finding max**: O(k), where k is number of unique phone numbers
- **Overall Time Complexity**: O(m + k)
- **Justification**: Single pass through data, dictionary operations are constant time, and finding the max is linear in the number of entries.


## Task3

**Description**:
- **Part A**: Identify all unique area codes and mobile prefixes called by Bangalore fixed lines (starting with `(080)`).
- **Part B**: Calculate the percentage of these calls that were made to other Bangalore fixed lines.

**Approach**:
- Loop through all call records.
- For each caller starting with `(080)`, extract the appropriate code from the receiver number.
- Track how many calls from Bangalore were to Bangalore.

**Complexity Analysis**:
- **Looping through calls**: O(m)
- **Code parsing and set insertion**: O(1) average
- **Sorting area codes**: O(k log k), where k is number of unique codes
- **Overall Time Complexity**: O(m + k log k)
- **Justification**: One pass through the data, with minimal overhead besides sorting.


## Task4

**Description**: Identify potential telemarketers — numbers that **only make outgoing calls** and never receive calls or send/receive texts.

**Approach**:
- Create a set of all callers.
- Create another set of numbers that either send texts, receive texts, or receive calls.
- Subtract the second set from the first.
- Sort and print.

**Complexity Analysis**:
- **Looping through calls and texts**: O(n + m)
- **Set operations (insertion, subtraction)**: O(1) average per item
- **Sorting result set**: O(k log k), where k is number of suspected telemarketers
- **Overall Time Complexity**: O(n + m + k log k)
- **Justification**: Efficient data structures and a single pass through each dataset.
