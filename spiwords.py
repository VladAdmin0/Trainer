# Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed. Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.
sentence = input('enter:')


def spin_words(sentence):
    res = ""
    sentence = sentence.split(' ')
    for word in sentence:
        # print(word)
        if len(word) >= 5:
            drow = word[::-1]
            res += drow + " "
            # print(res)
        else:
            res += word + " "

    res = res.rstrip()
    print(res)











spin_words(sentence)