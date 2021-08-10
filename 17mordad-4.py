nterms = 5
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count<nterms:
    print(n1)
    x=n1+n2
    n1=n2
    n2=x
    count += 1
print((x-1)/count)