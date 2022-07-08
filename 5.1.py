def main():
    A = [0,1,2,0,2,1,1]
    i = 3

    quicksort_basic(A,i)
    quicksort(A,i)
    quicksort_EPI(A,i)
    quicksort_EPI2(A, i)
    # print("reversed(range(len(A))):",reversed(range(len(A))))
    # x = [x for x in reversed(range(len(A)))]
    # print(x)

def quicksort_basic(A,i):
    print("basic:")
    print("A before:", A)
    print("pivot:", i)

    less, equal, more = [],[],[]

    pivot = A[i]

    for i in range(0,len(A)):
        if A[i] < pivot:
            less.append(A[i])
        elif A[i] == pivot:
            equal.append(A[i])
        else:
            more.append(A[i])

    A = less + equal + more

    print("A after:", A)


def quicksort(A,i):     # RB Solution - Doesn't work
    print("RB:")
    print("A before:",A)
    print("pivot:",i)

    left, right = 0, len(A) - 1

    pivot = A[i]

    while left < right:
        if A[left] < pivot:
            left += 1
        else:
            A[left], A[right] = A[right], A[left]
            right -=1

    print("A after:",A)

def quicksort_EPI(A,pivot_index): # EPI Solution
    print("EPI:")
    print("A before:", A)
    print("pivot:", pivot_index)

    pivot = A[pivot_index]

    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

    print("A after:", A)

def quicksort_EPI2(A,pivot_index): # EPI Solution
    print("EPI2:")
    print("A before:", A)
    print("pivot:", pivot_index)

    pivot = A[pivot_index]

    smaller = 0

    for i in range(len(A)):
        if A[i] < pivot:
            A[i],A[smaller] = A[smaller],A[i]
            smaller+=1

    larger = len(A) - 1

    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i],A[larger] = A[larger],A[i]
            larger -= 1

    print("A after:", A)

if __name__ == "__main__":
    main()