def cipher(target):
    output = ""
    for char in target:
        if char.islower():
            output += chr(219 - ord(char))
        else:
            output += char
    return output

print("文字列を入力：")
result = cipher(input())

print("暗号化: {}".format(result))
print("複合化: {}".format(cipher(result)))
