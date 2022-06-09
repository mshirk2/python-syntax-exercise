def print_upper_words(words):
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    for word in words:
        word.upper()
        if word[0] == "E":
            print(word.upper())


def print_upper_words3(words, letter):
    new_words = ''
    for word in words:
        word = word.upper()
        if word[0] == letter.upper():
            new_words.append(word)
    print(new_words)