def checkFibonacci(N):
        # code here 
        a,b =0,1
        if N in (a,b):
            return "Yes"
        while N>b:
            a,b =b,a+b
            if b==N:
                return "Yes"
        return "No"
N =11
flag =checkFibonacci(N)
print(flag)