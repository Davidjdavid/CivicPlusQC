import re

# Define a pattern that matches phone numbers but excludes the ###-###-#### format
phone_pattern = re.compile(r'\b(?!\d{3}-\d{3}-\d{4}\b)\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b')

# Test strings
test_strings = [
    "This is a correctly formatted number: 123-456-7890",
    "This is not correctly formatted: 123.456.7890",
    "Also not correct: 123 456 7890",
    "Incorrect too: 1234567890",
    "Mixed separators: 123-456.7890"
]

# Find matches
for test_string in test_strings:
    matches = phone_pattern.findall(test_string)
    if matches:
        print(f"Found incorrect phone number(s) in '{test_string}': {matches}")
    else:
        print(f"No incorrect phone numbers found in '{test_string}'")
