def twoSum1(arr,sum):
    pairs = []
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==sum:
                pairs.append([arr[i],arr[j]])
    return pairs

arr = [1,5,7,-1,5]
sum = 6
pairs = twoSum1(arr,sum)
print(pairs)