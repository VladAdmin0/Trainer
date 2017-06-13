# Jaden is also known for some of his philosophy that he delivers via Twitter. When writing on Twitter,
# he is known for almost always capitalizing every word.
#
# Your task is to convert strings to how they would be written by Jaden Smith.
# The strings are actual quotes from Jaden Smith, but they are not capitalized in the same way he originally typed them.
# Example:
# Not Jaden-Cased: "How can mirrors be real if our eyes aren't real"
# Jaden-Cased:     "How Can Mirrors Be Real If Our Eyes Aren't Real"
string = input('enter:')


def toJadenCase(string):
    string = string.title()
    string = string.replace("'T", "'t")
    string = string.replace("'Re", "'re")
    string = string.replace("'S", "'s")
    string = string.replace("'Ll", "'ll")
    string = string.replace("'M", "'m")
    print(string)
    return string






toJadenCase(string)