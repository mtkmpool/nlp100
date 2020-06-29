STR = ("Now I need a drink, alcoholic of course, "
       "after the heavy lectures involving quantum mechanics.")
result = [len(w) - w.count(',')-w.count('.') for w in STR.split()]
print(result)
