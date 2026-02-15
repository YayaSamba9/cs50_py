def ask_user():
    text = input("enter your text: ")
    # print(text.upper())
    return text


def modify():
    mod = ask_user()
    print ("The modification is: ",mod.upper())
    

def main():
    modify()

main()