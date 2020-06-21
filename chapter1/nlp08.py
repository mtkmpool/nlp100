
def cipher (text):
    result = ""
    for w in text:
        if w.islower():
            result = (219 - ord(w))
        else:
            result = w
    
    return result

text = "I am a one of the member of smmlab"
print (cipher(text))
