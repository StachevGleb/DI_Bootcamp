word = input("Insert word, but it's must be 10 characters long: ")
spec_char = f"{word[-1]}, {word[0]}"
if len(word) < 10:
    print("Word not long enough")
elif len(word) > 10:
    print("string too long")

print(spec_char)

x = ''
for element in range(0, len(word)):
    x += word[element]
    print(x)

