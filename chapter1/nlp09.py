"""This is a test program."""
import random

def typoglycemia(text):
    """typoglycemiaの定義"""
    result = []
    for word in text.split(' '):
        if len(word) < 5:
            result.append(word)
        else:
            middle = list(word)[1:-1]
            random.shuffle(middle)
            result.append(word[0] + ''.join(middle) + word[-1])
    return ' '.join(result)

str = ('I couldn’t believe that I could actually understand what I was reading : '
      'the phenomenal power of the human mind.')
print(typoglycemia(str))
