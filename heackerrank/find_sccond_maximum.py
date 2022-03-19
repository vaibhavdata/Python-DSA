if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(arr)
list_array = list(arr)
print(max([x for x in list_array if x != max(list_array)]))