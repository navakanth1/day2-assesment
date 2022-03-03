#wap to print all the prime numbers between 2-500
n1 = 2
n2 = 500
for i in range(n1,n2+1):
    k = 0
    for j in range(2,i//2+1):
        if(i%j==0):
            k=k+1
    if(k<=0):
        print(i)