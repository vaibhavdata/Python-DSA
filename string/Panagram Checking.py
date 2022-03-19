def panagramCheck(s):
    alpha= "abcdefghijklmnopqrstuvwxyz"
    if set(s.lower())==set(alpha):
        return 1
    else:
        return 0
s = 'Thequickbrownfoxjumpsoverthelazydog'
print(panagramCheck(s))