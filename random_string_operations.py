import functools
import string


def main():
    s = "string"
    # palindrome(s)

    a = "abcdef"
    b = "bcd"

    x = "123"
    y = '-123'

    # test_in_method(a,b)

    # random string operations

    # print(3 * '01')
    # print(3 * s)
    # print(','.join(('i','am','alive')))
    # print("Name {name}, Rank {rank}".format(name='RB',rank='2'))


    print(functools.reduce(lambda sum,c:sum*10+string.digits.index(c),x[x[0]in'-+':],0))
    print(functools.reduce(lambda sum,c:sum*10+string.digits.index(c),y[y[0]in'-+':],0))
    # print(x[x[0]in'-+':])
    # print(y[y[0]in'-+':])

def palindrome(s):
    print("original string:",s)

    s_reverse = s[::-1]

    print("reversed string:",s_reverse)

def test_in_method(a,b):
    print("a:",a)
    print("b:",b)
    print("is b in a?",b in a)

if __name__ == "__main__":
    main()