import validators
def main():
    print(email_valid(input("What's your email adress? ")))


def email_valid(m):
    if validators.email(m):
        return "Valid"
    return "Invalid"


if __name__ == '__main__':
    main()
