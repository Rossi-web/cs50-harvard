text = input("Input: ")

print("Output: ", end="")

for x in text:
    if not x.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(x, end="")

print()

