open("text.txt")

print("File text: ")
print(open("text.txt").read())

search = "word1"
replaced = "word2"

with open("text.txt", "r") as f:
    data = f.read()
    data = data.replace(search, replaced)

with open("text.txt", "w") as f:
    f.write(data)



