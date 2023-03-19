def get(n,k):
    p = 0
    for i in n:
        p+=(int(i) * k)
    return str(p)
def superDigit(n, k):
    # Write your code here
    while int(n) > 9:
        n = get(n,k)
        k = 1
    return n
