with open("popular-names.txt") as data_file:
    for line in data_file:
        print(line.replace("\t", " "), end="")
