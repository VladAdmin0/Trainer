# Given two integers, which can be positive and negative, find the sum of all the numbers between including them
# too and return it. If both numbers are equal return a or b.
a = int(input('enter a:'))
b = int(input('enter b:'))


def get_sum(a,b):
    if a == b:
        # return a
        print(a)
    elif a < 0 and b > 0:
        counta = a
        countb = a + b
        c = 0
        d = 0
        while counta <= 0:
            c = a + c
            a += 1
            counta += 1
        while countb >= 0:
            d = b + d
            b -= 1
            countb -= 1
        print(c+d)
    elif b < 0 and a > 0:
        countb = b
        counta = b + a
        c = 0
        d = 0
        while countb <= 0:
            c = b + c
            b += 1
            countb += 1
        while counta >= 0:
            d = a + d
            a -= 1
            counta -= 1
        print(c+d)
    elif b < 0 and a < 0:
        if a < b:
            c = 0
            count = a - b
            while count <= 0:
                c = b + c
                count += 1
                b -= 1
            print(c)
        elif b < a:
            count = b - a
            c = 0
            while count <= 0:
                c = a + c
                count += 1
                a -= 1
            print(c)
    elif b > 0 and a > 0:
        if a < b:
            count = b-a
            c = 0
            while count >= 0:
                c = a + c
                count -= 1
                a += 1
            print(c)
        elif b < a:
            count = a - b
            c = 0
            while count >= 0:
                c = b + c
                b += 1
                count -= 1
            print(c)
    else:
        print(a+b)

get_sum(a,b)

