from random import randint
while True:
    try:
        level = int(input("Level: "))
        if level > 0 :
            break
    except:
        pass
    nblimit = randint(1,level)
    try:
        guess = int(input("Guess: "))
        if guess <0 :
            continue
        else:
            if guess < nblimit :
                print("Too Small")
            elif guess > nblimit:
                print("Too large")
            else:
                print("Just right")
                break
    except EOFError:
        pass


