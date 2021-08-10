nterms = 100
n1, n2 = 0, 1
count = 0
while count<nterms:
    x=n1+n2
    n1=n2
    n2=x
    count += 1
print((x-1)/count)