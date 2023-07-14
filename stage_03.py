with open("artifact.txt","r") as f:
    text=f.read()

with open("artifact.txt","w") as f:
    f.write(text+"i have added oone line ")

print(text)
print("it end of stage 3")