
def get_input_num():
    in_num = input("Input number : ")
    try :
        num = int(in_num)
        return num
    except:
        print(f"Input is not numberic")
    return 0;

def generate_mul_table(num:int):
    for i in range(1,13):
        print(f"{num} x {i} = {num*i}")

number = get_input_num()
generate_mul_table(number)