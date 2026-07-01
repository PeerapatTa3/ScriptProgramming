
def get_user_input():
    try:
        user_age = int(input('Input your number : '))
        return user_age
    except:
        print(f"The input is not numberic")

def recom_base_on_age(age):
    if 0 < age < 5 :
        print(f"You're too young for movies! Enjoy cartoons.")
    elif 5 <= age <= 12:
        print(f"G-rated or PG-rated movies.")
    elif 13 <= age <= 17:
        print(f"PG-13 or R-rated movies (with parental guidance).")
    elif age >= 18:
        print(f"Any movie rating.")
        ans: str = input("Do you like action moveis? (yes/no) : ")
        if ans.lower() == "yes":
            print("You might enjoy the lastest action blockbuster!.")
        else :
            print("oke.")
    else:
        print("Negative age! Are you sure that's your age?")

recom_base_on_age(get_user_input())