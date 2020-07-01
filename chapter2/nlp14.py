import sys

def readline(file_name):
    with open(file_name, "r") as target_file:
        return target_file.readlines()

file_name = sys.argv[1]
N = sys.argv[2]

target_lines = readline(file_name)

print("".join(target_lines[:int(N)]))
