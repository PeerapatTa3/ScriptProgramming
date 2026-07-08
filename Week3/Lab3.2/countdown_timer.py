def get_input_num():
    in_num = input("Input number : ")
    try :
        num = int(in_num)
        return num
    except:
        print(f"Input is not numberic")
    return 0;

def countdown_timer(num: int):
    while num>=0:
        print(f"{num}")
        num -= 1
    print("Blast off!")

number = get_input_num()
countdown_timer(number)