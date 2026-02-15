text = input("Put your text please: ")
voyels = "aiuoeAIUOE"
txt = ""
for i in text :
    if i not in voyels:
        txt +=i
print(txt,end=" ")