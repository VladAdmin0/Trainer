# Welcome. In this kata you are required to, given a string,
# replace every letter with its position in the alphabet. If anything in the text isn't a letter,
# ignore it and don't return it. a being 1, b being 2, etc
text = input('enter text:')


def alphabet_position(text):
    text = text.upper()
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z']
    res = ""
    result = [x for x in text if x in alphabet]
    # for x in result:
    #     if x in alphabet:
    #         indx = alphabet.index(x)
    #         indx += 1
    #         newtext.append(indx)
    for x in result:
        if x in alphabet:
            indx = alphabet.index(x)
            indx += 1
            indx = str(indx)
            res += indx + " "
    res = res.rstrip()
    print(res)


alphabet_position(text)