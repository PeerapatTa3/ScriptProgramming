#Activity 3.1

# Python
# Buggy Snippet A: Infinite Loop
counter = 0
while counter < 5:
    print(counter)
    counter += 1 #<-add increment
     # Missing counter increment!

# Buggy Snippet B: Incorrect Range
for i in range(1, 6): # Goal: print 1, 2, 3, 4, 5
    print(i,end=", ")

# Buggy Snippet C: Misplaced Break
for char in "hello":
    print(char) # This will print 'h', 'e', 'l' then break
    if char == 'l':
        print("Found 'l', stopping!")
        break

#Activity 3.2 สิ่งที่อยากให้ทำคือ

def asterisks_squ(height,width):
    for i in range(0,height):
        for j in range(0,width):
            print("*",end="")
        print("\n")

asterisks_squ(5,5)