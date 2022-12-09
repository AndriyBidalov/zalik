print(open("text.txt").read())

search = input("Will be replaced: ")
replace = input("Word that replace: ")

with open("text.txt", "r") as f:
    data = f.read()
    data = data.replace(search, replace)

with open("text.txt", "w") as f:
    f.write(data)

open("text.txt")

print(open("text.txt").read())

