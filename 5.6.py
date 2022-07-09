def main():
    A = [310,315,275,295,260,270,290,230,255,250]

    maxprofit_RB_bruteforce(A)

def maxprofit_RB_bruteforce(A):

    max_profit = 0

    for i in range(0,len(A)-1):
        for j in range(i,len(A)-1):
            if A[j] - A[i] > max_profit:
                max_profit = A[j] - A[i]

    print(max_profit)

if __name__ == "__main__":
    main()