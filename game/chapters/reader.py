file = open("text.txt")
c = ""
index = 0



characters = {"Catalina" : "c", "Valencia" : "v", "Maximiano" : "m", "Diedriech" : "d", "Edmundo" : "e"}

print()
for line in file:
    if(line[0] == "["):
        for x in line[1:]:
            index += 1
            if x == "]":
                index +=2
                break
            c = c + x


        if(c.split(" ")[0] in characters.keys()):
            c = c.split(" ")[0]
            print(characters[c], line[index:-1])
        else:
            print("\"" + c + "\" " + line[index:-1])

        c = ""
        index = 0

    else:
        print("\"" + line[:-1] + "\"")
print()
