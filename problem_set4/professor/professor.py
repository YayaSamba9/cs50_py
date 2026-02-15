# import random


# def main():
#     ...


# def get_level():
#     while True :
#         try:
#             level = int(input("Level: "))
#             if level in [1,2,3]:
#                 break
#         except:
#             pass
#     return level



# def generate_integer(level):
#     if level == 1:
#         nbr1 = random.randint(1,9)
#         nbr2 = random.randint(1,9)
#     elif level == 2:
#         nbr1 = random.randint(10,99)
#         nbr2 = random.randint(10,99)
#     else:
#         nbr1 = random.randint(100,999)
#         nbr2 = random.randint(100,999)

    
#     return nbr1,nbr2



# if __name__ == "__main__":
#     main()

import contextlib
import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        with contextlib.suppress(ValueError):
            level = int(input("Level: "))
            if level in {1, 2, 3}:
                return level
            else:
                raise ValueError


def generate_integer(level):
    user_score = 0
    for _ in range(1, 11):
        if level == 1:
            X = random.randint(0, 9)
            Y = random.randint(0, 9)
        elif level == 2:
            X = random.randint(10, 99)
            Y = random.randint(10, 99)
        else:
            X = random.randint(100, 999)
            Y = random.randint(100, 999)

        user_tries = 1
        while user_tries <= 3:
            try:
                user_answer = int(input(f"{X} + {Y} = "))
            except ValueError:
                print("EEE")
                user_tries += 1
                continue
            else:
                real_answer = X + Y
                if user_answer == real_answer:
                    user_score += 1
                    break
                else:
                    print("EEE")
                    if user_tries == 3:
                        print(f"{X} + {Y} = {real_answer}")
                    user_tries += 1
    print()
    print(f"Score: {user_score}")


if __name__ == "__main__":
    main()
