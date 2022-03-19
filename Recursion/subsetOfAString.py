def subsetOfAString(ip,op):
    if len(ip)==0:
        print("Straing",op)
        return op
    
    subsetOfAString(ip[1:],op+ip[0])
    subsetOfAString(ip[1:],op)
    
    
    

ip ='abcd'
op =''
subsetOfAString(ip,op)