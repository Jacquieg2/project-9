# Author: Jacqueline Garcia
# GitHub username: Jgarcia2
# Date: 03/04/2025
# Description: Counting letters.

def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            upper_char = char.upper()  # Convert to uppercase
            letter_counts[upper_char] = letter_counts.get(upper_char, 0) + 1
    return letter_counts
