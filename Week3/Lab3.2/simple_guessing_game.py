
def get_input_num():
    in_num = input("Input number : ")
    try :
        num = int(in_num)
        return num
    except:
        print(f"Input is not numberic")
        return None;
    
def guess_num():
    num:int = 0
    secret_number:int = 42
    max_guess = 5
    guess = max_guess

    while True:
        print(f"Current guess({guess}/{max_guess})")
        num = get_input_num()
        try:
            if num == secret_number:
                print("Congratulations! You guessed it!")
                break
            elif num < secret_number:
                print(f"{num} is too low! Try again.")
            else :
                print(f"{num} is too high! Try again.")

            guess -= 1

            if guess <= 0:
                print("You used UP all guess!")
                break
        except:
            continue
            
guess_num()