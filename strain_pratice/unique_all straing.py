def uniqueAllChar(ip_str):
    unique_str = set(ip_str)
    if len(ip_str) ==len(unique_str):
        return True
    else:
        return False
ip_str = "abcdd"
flag = uniqueAllChar(ip_str)
print(flag)
