hash_map ={}
def subStraing(ip,op):
    if len(ip)==0:
        hash_map[op] =1
        return 
    subStraing(ip[1:],op+ip[0])
    subStraing(ip[1:],op)
ip = "abcccddabb"
op =""
subStraing(ip,op)
print(list(hash_map.keys()))