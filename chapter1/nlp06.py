
STR1 = "paraparaparadise"
STR2 = "paragraph"

def n_gram_chara(input_str, num):
    result = []
    for i in range(len(input_str)- num + 1):
        result.append(input_str[i: i + num])
    return result

X = set((n_gram_chara(STR1, 2)))
Y = set((n_gram_chara(STR2, 2)))

# print (X)
# print (Y)
print(X | Y)
print(X & Y)
print(X - Y)
print('se' in X)
print('se' in Y)
