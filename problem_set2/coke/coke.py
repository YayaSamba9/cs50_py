amount_due = 50
print(amount_due)
while amount_due > 0 :

    coin = int(input("Put your coin: "))
    if coin in [25,10,5]:
        amount_due -= coin
        print("Amount_due", str(amount_due))
    else:
        print("You may put a good coin please")

co = abs(amount_due)
print(co)
