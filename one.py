import random
a=1
while True:
    b=random.randint(1,6)
    c=int(input("plz Enter a number :"))
    if b==c:
        print("you win",a,"times")
        break
    else:        
        print("you are loser")
        a+=1