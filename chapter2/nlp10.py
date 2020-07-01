COUNT = 0
text_file = open("popular-names.txt", "rt")

for line in text_file:
    COUNT += 1

print(COUNT)
