

with open('books/frankenstein.txt') as f:
    text = f.read()
    
    text_lower = text.lower()

    # make a dictionary of letters and their frequencies
    letter_freq = {}
    for letter in text_lower:
        if letter.isalpha():
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

    # convert dictionary into list of tuples
    letter_freq = list(letter_freq.items())

    # sort list of tuples by frequency
    letter_freq.sort(key=lambda x: x[1], reverse=True)

    print("---Book letter frequency report---")
    # print all the results, 1 per line
    for letter, freq in letter_freq:
        print(f"The letter {letter} occurs {freq} times")


