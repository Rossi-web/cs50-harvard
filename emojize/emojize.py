import emoji

x = input("Input: ").lower().strip()

output = emoji.emojize(x)
print("Output: ",output)