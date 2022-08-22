from random import*
name1 = input("Enter name 1:")
name2 = input("Enter name 2:")
for i in range(5):

    a = randint(1,6)
    b = randint(1,6)
    x = randint(1,6)
    y = randint(1,6)
    print(f"{name1} = {a},{b}\t{name2} = {x},{y}")
    if a == b and x==y:
        print("draw! ,run program again")
        
        break
    elif a == b:
        print(f"{name1} is winner!!\nYou can run program again")
    elif x == y:
        print(f"{name2} is winner!!\nYou can run program again")
        break
else:
    print("No one won, Run the program again!")
    
    