def main():
    A = [310,315,275,295,260,270,290,230,255,250]

    maxprofit_RB_bruteforce(A)
    maxprofit_EPI(A)

def maxprofit_RB_bruteforce(A):

    max_profit = 0

    for i in range(0,len(A)-1):
        for j in range(i,len(A)-1):
            if A[j] > A[i]:
                if A[j] - A[i] > max_profit:
                    max_profit = A[j] - A[i]

    print("max profit brute force = ",max_profit)

def maxprofit_EPI(A):

    min_price_so_far = float('inf')
    max_profit_so_far = 0

    for price in A:
        max_profit_sell_today = price - min_price_so_far
        max_profit_so_far = max(max_profit_so_far, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far,price)

    print("max profit EPI = ",max_profit_so_far)

if __name__ == "__main__":
    main()