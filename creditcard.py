# My task is to write a function maskify, which changes all but the last four characters into '#'.
# "sgdfgsdsgndthndtn"
cc = input('enter:')


def maskify(cc):
    val = len(cc)
    if val < 4:
        return cc
    else:
        four = cc[-4:]
        new = '#'*(len(cc)-4)
        cc = new + four
        print(cc)
        return cc

maskify(cc)

