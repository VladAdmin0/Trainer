# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.
string = input('enter word:')


def is_isogram(string):
    string = string.lower()

    if string.isdigit() == True:
        print('False')

    elif string == "":
        print('True')

    else:
        lenstr = len(string)
        newstr = []
        for i in string:
            newstr += i
        lennew = len(set(newstr))
        if lenstr == lennew:
            print('True')
        else:
            print('False')


is_isogram(string)
