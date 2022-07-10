import functools
import string


def main():

    x = 123
    y = -123

    a = '123'
    b = '-123'

    # print("int to string")
    # int_to_string(x)
    # int_to_string(y)
    #
    # print(' ')

    print("string to int")
    string_to_int(a)
    string_to_int(b)

def int_to_string(x: int) -> str:
    print("input:",x,"input type:",type(x))

    is_neg = False

    if x < 0:
        is_neg = True
        x = -x

    ans = []

    while True:
        ans.append(chr(ord('0') + x % 10))
        x = x // 10
        if x == 0:
            break

    # ''.join(reversed(ans))
    # if is_neg:
    #     ans = '-' + ()
    # else:
    #     ans = '' + ans

    ans = ('-' if is_neg else '') + ''.join(reversed(ans))

    print("output:",ans,"output type:",type(ans))

def string_to_int(a: str) -> int:
    print("input:", a, "input type:", type(a))

    if a[0] == '-':
        ans = -1
    else:
        ans = 1

    ans = ans * functools.reduce(lambda cum_sum,x: cum_sum*10 + string.digits.index(x),a[a[0]in'-+':],0)

    print("output:", ans, "output type:", type(ans))

if __name__ == "__main__":
    main()