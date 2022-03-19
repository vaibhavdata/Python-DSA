def checkfibnoic(n):
    a =0
    b =1
    
    if n==1:
        return 0
    if n==2:
        return 1

    return (checkfibnoic(n-1)+checkfibnoic(n-2))%1000000007
n =5


