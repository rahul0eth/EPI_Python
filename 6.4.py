def main():
    a = ["a","c","d","b","b","c","a"]

    replace_remove(a,7)

def replace_remove(s,n):

    print('before:',s)

    write_index = 0
    a_count = 0

    for i in range(n):
        if s[i] != 'b':
            s[write_index] = s[i]
            write_index += 1
        if s[i] == 'a':
            a_count += 1

    #iterate in reverse
    current_index = write_index -1
    write_index += a_count -1
    final_size = write_index + 1

    while current_index >= 0:
        if s[current_index] == 'a':
            s[write_index - 1:write_index+1] = 'dd'
            write_index -= 2
        else:
            s[write_index] = s[current_index]
            write_index -= 1
        current_index -= 1

    print('after:',s)

if __name__ == "__main__":
    main()