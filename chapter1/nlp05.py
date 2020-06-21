#st = "I am an NLPer"
#word = st.split()
#r = range(len(word))
#print (list(r))

def n_gram_word (str, n):
    words = str.split()
    result = []
    for i in range(len(words)-n+1):
        result.append(words[i: i+n])
    
    return result

def n_gram_chara (str, n):
    result = []
    for i in range(len(str)-n+1):
        result.append(str[i: i+n])
    
    return result

print(n_gram_word("I am an NLPer",2))
print(n_gram_chara("I am an NLPer",2))
