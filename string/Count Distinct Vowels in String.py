def countVowel(s):
    vowel = "AaEeIiOoUu"
    res = set([chr for chr in s if chr in vowel])
    return len(res)
s = "GeeksForGEeks"
print(countVowel(s))