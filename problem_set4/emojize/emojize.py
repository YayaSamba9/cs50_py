import emoji

user_answer = input("Input: ")
answer = emoji.emojize(user_answer,language= "alias")
print("Output:" + answer)
