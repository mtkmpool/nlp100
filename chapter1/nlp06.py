
str1 = "paraparaparadise"
str2 = "paragraph"

def n_gram_chara (str, n):
    result = []
    for i in range(len(str)- n + 1):
        result.append(str[i: i + n])
    
    return result

X = set((n_gram_chara(str1,2)))
Y = set((n_gram_chara(str2,2)))

# print (X)
# print (Y)
print (X | Y)
print (X & Y)
print (X - Y)
print ('se' in (X))
print ('se' in (Y))