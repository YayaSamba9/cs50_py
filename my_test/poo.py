def main():
    back = get_student()
    if back[0]=="Yahya":
        back[1] = "COULIBALY"
    print(type(back))
    print(f"my name is {back[0]} and my sirname {back[1]} ")




def get_student():
    name = input("Name: ")
    sirname = input("Sirname: ")
    return name,sirname




if __name__ == "__main__":
    main()