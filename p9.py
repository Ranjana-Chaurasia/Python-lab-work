# Text Anagram and Pattern Matcher Tool
import re
from collections import Counter

# Function 1: Clean text by removing spaces and punctuation
# Convert text to lowercase for case-insensitive comparison
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]", "", text)
    return text

# Function 2: Check whether two texts are anagrams using sorting
def are_anagrams(text1, text2):
    cleaned1 = clean_text(text1)
    cleaned2 = clean_text(text2)

    if not cleaned1 or not cleaned2:
        return False
    return sorted(cleaned1) == sorted(cleaned2)

# Function 3: Check anagrams using dictionary character counting
def are_anagrams_counting(text1, text2):
    cleaned1 = clean_text(text1)
    cleaned2 = clean_text(text2)

    if not cleaned1 or not cleaned2:
        return False
    return Counter(cleaned1) == Counter(cleaned2)

# Function 4: Generate an immutable tuple key
# The tuple represents the sorted characters of the cleaned text
def generate_anagram_key(text):
    cleaned = clean_text(text)
    return tuple(sorted(cleaned))

# Function 5: Group anagrams using dictionary and tuple keys
def group_anagrams(words):
    groups = {}
    for word in words:
        cleaned = clean_text(word)
        if not cleaned:
            continue
        key = generate_anagram_key(word)

        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return list(groups.values())

# Function 6: Generate a character pattern for a word
def generate_pattern(text):
    cleaned = clean_text(text)
    pattern = {}
    result = []

    for char in cleaned:
        if char not in pattern:
            pattern[char] = len(pattern)
        result.append(pattern[char])
    return tuple(result)

# Function 7: Match words with the same character pattern
def match_patterns(words, target):
    target_pattern = generate_pattern(target)
    matches = []

    for word in words:
        if clean_text(word) and generate_pattern(word) == target_pattern:
            matches.append(word)
    return matches

# Main program
def main():
    print("=" * 45)
    print("TEXT ANAGRAM AND PATTERN MATCHER TOOL")
    print("=" * 45)

    while True:
        print("\nChoose an operation:")
        print("1. Check anagram using sorting")
        print("2. Check anagram using character counting")
        print("3. Group anagrams")
        print("4. Match character patterns")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            text1 = input("Enter the first word or phrase: ")
            text2 = input("Enter the second word or phrase: ")
            if are_anagrams(text1, text2):
                print("Result: The texts are anagrams.")
            else:
                print("Result: The texts are not anagrams.")

        elif choice == "2":
            text1 = input("Enter the first word or phrase: ")
            text2 = input("Enter the second word or phrase: ")
            if are_anagrams_counting(text1, text2):
                print("Result: The texts are anagrams.")
            else:
                print("Result: The texts are not anagrams.")

        elif choice == "3":
            user_input = input(
                "Enter words separated by commas: "
            )
            words = [word.strip() for word in user_input.split(",")]
            groups = group_anagrams(words)
            print("\nAnagram Groups:")
            for group in groups:
                print(group)

        elif choice == "4":
            user_input = input(
                "Enter words separated by commas: "
            )
            words = [word.strip() for word in user_input.split(",")]
            target = input("Enter the target pattern word: ")
            matches = match_patterns(words, target)
            print("\nWords matching the target pattern:")
            if matches:
                print(matches)
            else:
                print("No matching words found.")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()