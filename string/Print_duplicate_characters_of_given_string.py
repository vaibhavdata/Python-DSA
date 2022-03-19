# first method duplicate char
def duplicatedCharPrint(ip_str):
    count =[]
    for i in list(set(ip_str)):
        c = 0
        for j in ip_str:
            if i==j:
                c= c+1
        count.append([i,c])
    ans =[]
    for chr,cou in count:
        if cou >1:
            ans.append(chr)
    return ans
ip_str = 'abababccdddffgghhjkkvkvcdlg'
op_str = duplicatedCharPrint(ip_str)
print(op_str)

print("Second method of print duplicated")

def printDuplicatedChar2(ip_str):
    count ={}
    for i in ip_str:
        if i in count:
            count[i] = count[i]+1
        else:
            count[i]=1
    ans = []
    for char,coun in count.items():
        if coun >1:
            ans.append(char)
    return ans

ip_str = 'abababcvcdlg'
op_str = duplicatedCharPrint(ip_str)
print(op_str)
