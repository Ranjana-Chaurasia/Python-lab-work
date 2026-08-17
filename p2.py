# Automated Word Frequency & Pattern Analyzer
import string

def analyze_text(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    total_words = len(words)

    # Dictionary to store the frequency of each word
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    palindromes = []

    for word in frequency:
        # A palindrome reads the same forwards and backwards
        if len(word) > 1 and word == word[::-1]:
            palindromes.append(word)

    return total_words, frequency, palindromes


def main():
    print("=== Word Frequency & Pattern Analyzer ===")

    print("Enter your text.")
    print("Type END on a new line when you are finished.\n")

    lines = []

    while True:
        line = input()

        # Stop taking input when the user types END
        if line == "END":
            break
        lines.append(line)

    text = " ".join(lines)

    total_words, frequency, palindromes = analyze_text(text)

    print("\n========== ANALYSIS REPORT ==========")
    print("Total words:", total_words)
    print("\nWord Frequency:")

    # Display each word and its frequency
    for word, count in sorted(frequency.items()):
        print(f"{word}: {count}")
    print("\nPalindrome Words:")
    if palindromes:
        print(", ".join(sorted(palindromes)))
    else:
        print("No palindrome words found.")
    print("======================================")

if __name__ == "__main__":
    main()