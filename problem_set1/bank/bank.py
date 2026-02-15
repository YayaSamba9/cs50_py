answer = input("Greeting: ").lower()

if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$40")
else:
    print("$100")
