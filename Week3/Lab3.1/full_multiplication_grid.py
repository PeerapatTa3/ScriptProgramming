def full_mul_grid():
    for i in range(1,13):
        for j in range(1,13):
            print(f"{i*j:4d}",end = "")
        print("\n")

print("Full Multiplicaiton Grid")
full_mul_grid()