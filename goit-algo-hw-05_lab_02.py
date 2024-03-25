import re

def generator_numbers(text):
    pattern = r'\b\d+\.\d+\b'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text):
    return sum(generator_numbers(text))

# Приклад використання
text = "The total income of an employee consists of several parts 1000.01 as the main income supplemented by additional income 351.45 dollars."
total_profit = sum_profit(text)
print(f"Total profit: {total_profit}")
