from random import*
x1 = "sang"
x2 = "kaghaz"
x3 = "gheichi"
x = input("in ye bazie sang, kaqaz, gheichi, hast! yek kodom ro entekhab kon! baraye kharej shodan az barname 'exit' ro type kon\n")
while True:
    
    if x == "exit":
        exit()
    y = randint(1,4)
    if y ==1:
        print("robot:",x1)
    elif y ==2:
        print("robot:",x2)
    elif y ==3:
        print("robot:",x3)
    if x == "kaghaz" and y ==1:
        print("bordi!\n")
    elif x == "kaghaz" and y ==2:
        print("mosavi shod!\n")
    elif x == "kaghaz" and y ==3:
        print("bakhti!\n")
    elif x == "sang" and y==1:
        print("mosavi shod!\n")
    elif x == "sang" and y==2:
        print("bakhti!\n")
    elif x == "sang" and y==3:
        print("bordi!\n")
    elif x == "gheichi" and y ==1:
        print("bakhti!\b")
    elif x == "gheichi" and y ==2:
        print("bordi!\b")
    elif x == "gheichi" and y ==3:
        print("mosavi shod!\b")
    
    j = input("dobare entekhab kon !\n")
