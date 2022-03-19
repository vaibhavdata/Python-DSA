def nextAlphabeticalElement(string,key,start,end):
    res = -1
    while start < end:
        mid = (start + end)//2
        if string[mid]==key:
            start = mid +1
        elif key<string[mid]:
            res = string[mid]
            end = mid-1
        elif key> string[mid]:
            start =mid+1
    return res

string = "abcehi"
key="d"
start = 0
end =len(string)-1
alpha =nextAlphabeticalElement(string,key,start,end)
print(alpha)
print()

def nextAlphabeticalElement(string,key,start,end):
    res = -1
    while start <= end:
        mid = (start+end)//2 
        if key==string[mid]:
            start = mid+1
        elif key < string[mid]:
            res = string[mid]
            end = mid-1  
        elif key > string[mid]:
            start = mid+1
    return res

string = 'abchjoqt'
key = 'l'
start = 0
end = len(string)-1
nextAlpha = nextAlphabeticalElement(string,key,start,end)
print(nextAlpha)
print()
def nextAlphabeticalElement(straing,key,start,end):
    res = -1
    while start < end:
        mid = (start+end)//2
        if key == straing[mid]:
            start = mid+1
        elif key < straing[mid]:
            res = straing[mid] # res =mid count number meansindex number
            #res= mid
            end = mid-1
        elif key > straing[mid]:
            start = mid+1
    return res
straing = 'abcjptw'
key = 'q'
start = 0
end = len(straing)-1
nextalpha =  nextAlphabeticalElement(straing,key,start,end)
print(nextalpha)
