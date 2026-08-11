## Printing numbers from n to 1 using recursion

def countdown(n):
    if n == 0:
        print("Done!")   # base case
    else:
        print(n)
        countdown(n - 1)  # recursive call

countdown(5)