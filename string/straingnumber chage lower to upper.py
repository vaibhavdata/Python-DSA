def straing_for(s):
    lower_char = []
    upper_char =[]
    even_digit =[]
    odd_digits =[]
    for char in s:
        if char.islower():
            lower_char.append(char)
        elif char.isupper():
            upper_char.append(char)
        elif char.isdigit():
            if int(char)%2==0:
                even_digit.append(char)
            else:
                odd_digits.append(char)
    return  ("".join(sorted(lower_char)+ sorted(upper_char)+sorted(odd_digits)+sorted(even_digit)))
    
if __name__ =="__main__":
    s = input()
    print(straing_for(s))