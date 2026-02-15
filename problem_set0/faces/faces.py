def convert(txt):
    txt = txt.replace(":)","🙂")
    txt = txt.replace(":(","🙁")
    return txt


def main():
    emotion = input("put your emotion: ")
    rslt = convert(emotion)
    print (rslt)



main()

