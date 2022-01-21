content = True
i = 1 

with open ("log.txt") as f:
    #i+=1
    while content:
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print("yes python is present")
            print(i)
            i+=1