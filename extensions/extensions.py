format = input("Digite o formato do seu arquivo: ").lower().strip()

if format.endswith(".gif"):
    print("image/gif")

elif format.endswith(".jpg"):
    print("image/jpeg")

elif format.endswith(".jpeg"):
    print("image/jpeg")

elif format.endswith(".png"):
    print("image/png")

elif format.endswith(".pdf"):
    print("application/pdf")

elif format.endswith(".txt"):
    print("text/plain")

elif format.endswith(".zip"):
    print("application/zip")

else:
    print("application/octet-stream")
