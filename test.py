search = "word1"
replace = "word2"

with open("text.txt", "r") as f:
    data = f.read()
    data = data.replace(search, replace)

with open("text.txt", "w") as f:
    f.write(data)

open("text.txt")

print("File text: ")
print(open("text.txt").read())



