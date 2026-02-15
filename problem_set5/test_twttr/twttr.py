def main ():
    text = input("Put your text please: ")
    print(shorten(text), end=" ")
  
    
def shorten (word):
    voyels = "aeoiuAEOIU"
    text = ""
    for i in word :
        if i not in voyels :
            text += i
    return text 


if  __name__ == "__main__" :
    main()