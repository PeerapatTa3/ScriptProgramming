
def get_user_input():
    try:
        user_num = int(input('Input your number : '))
        return user_num
    except:
        print(f"The input is not numberic")
    
def check_pos_neg(num):
    if num<0:
        return "negative"

    elif num>0:
        return "positive"
            
    else :
        return "zero"

def check_odd_even(num):
    if num%2 == 0:
        return "even"
    else:
       return "odd"

num = get_user_input()
print(f"The numver is {check_pos_neg(num)} and {check_odd_even(num)}.")