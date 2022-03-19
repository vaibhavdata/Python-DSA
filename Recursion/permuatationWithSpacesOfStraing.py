def permuatationWithSpaces(ip,op):
    if len(ip)==0:
        print(op)
        return 
    permuatationWithSpaces(ip[1:],op+" "+ip[0])
    permuatationWithSpaces(ip[1:],op+ip[0])


ip ="abbccd"
op = ""
permuatationWithSpaces(ip[1:],ip[0])
