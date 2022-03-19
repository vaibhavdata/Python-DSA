

def reversArray(ip_array):
    if len(ip_array)==1:
        return 
    alpha = ip_array.pop(0)
    reversArray(ip_array)
    ip_array.append(alpha)
ip_array = [3,4,5,6,7,8,9]
reversArray(ip_array)
print(ip_array)
print()
# second method 
def reverlist(list):
    return [ele for ele in reversed(list)]
list = [1,2,3,4,5,6]
reversed(list)
print(list)
print()
# thired method 
def reverslist(lis):
    new_list = lis[::-1]
    return new_list
lis = [3,4,5,6,7,8]
reverslist(lis)
print(lis)