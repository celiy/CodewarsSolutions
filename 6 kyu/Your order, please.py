#Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

#Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

#If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

def order(sentence):
    if len(sentence) == 0:
        return sentence

    words = sentence.split()
    sorted_words = [None] * len(words)

    for word in words:
        for char in word:
            if char.isdigit():
                sorted_words[int(char) - 1] = word
                break

    return " ".join(sorted_words)