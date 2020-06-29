#st = "I am an NLPer"
#word = st.split()
#r = range(len(word))
#print (list(r))

def n_gram_word(input_str, num):
    words = input_str.split()
    result = []
    for i in range(len(words)-num+1):
        result.append(words[i: i+num])
    return result

def n_gram_chara(input_str, num):
    result = []
    for i in range(len(input_str)-num+1):
        result.append(input_str[i: i+num])
    return result

print(n_gram_word("I am an NLPer", 2))
print(n_gram_chara("I am an NLPer", 2))
