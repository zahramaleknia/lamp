import random
def lamp():
    try:
        second=int(input("enter number"))
        if seconf<=0:
            print("enter new number")
            return
        count=0
        status=random.randint(0,1)
        print(f"first status:{ "on" if status==1 else "off" }")
        for i in range(second):
            switch=random.randint(0,1)
            if switch!=status:
                count+=1
                status=switch
            print("on"if switch==1 else "off")
        print(f"lamp chenge status:{count}")
    except ValueError:
        print("enter a number")
lamp()
