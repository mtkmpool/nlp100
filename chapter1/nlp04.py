str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = str.split ()
#print (words)
one_words= [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for (i, word) in enumerate(words):
#print ('{0}:{1}'.format(i,word))
    if i+1 in one_words:
        dic [i+1] = word[0] 
    else:
        dic [i+1] = word[:2]
print (dic)    

