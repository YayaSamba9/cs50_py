question = input("What's the answer to the great question of life ? ").lower()


    
if question == "42" :
    print("Yes")
elif  "Forty two":
    print("Yes")
elif "forty-two":
    print("Yes")
else :
    print("No")

# match question :
#     case "42" | "forty-two":
#         print("Yes")
#     case _:
#         print('No')