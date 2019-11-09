

import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        a=int(input("Enter 1 for Food and 2 for Exercise"))
        if b==1:
            value=input("Type here...")
            with open("Harry Food.txt","a") as op:
                    op.write(str([str(gettime())])+":" +value+"\n")
            print("Written Successfully")
        elif b==2:
            value=input("Type here...")
            with open ("Harry Exercise.txt","a") as op:
                 op.write(str([str(gettime())])+":"+value+"\n")
            print("Written Successfully...")
    elif k==2:
        a=int(input("Enter 1 for Food and 2 for Exercise"))
        if b==1:
            value=input("Type here...")
            with open("satyansh food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Written Successfully...")
        elif(b==2):
            value=input("Type here...")
            with open("satyansh excrcise.txt" ,"a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Written Successfully...")
    else:
        print("Please Valid enter [harry,satyansh]")
def retrive(k):
    int(input("Enter 1 for excrcise and 2 for Food"))
    if k==1:
        if b==1:
            with open("Harry Food.txt") as op:
                for i in op:
                    print(i,end="")
        elif b==2:
            with open("Harry Exercise.txt","a") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        if b==1:
            with open("satyansh food.txt") as op:
                for i in op:
                    print(i,end="")
        elif b==2:
            with open("satyansh exercise.txt","a") as op:
                for i in op:
                    print(i,end="")
    else:
        print("Please enter valid value:---->")
print("Heth Management System")
a=int(input("           Enter 1 for log value and press 2 for retrive value..."))
if a==1:
    b=int(input("       Press 1 for Harry and 2 for satyansh"))
    take(b)
else:
    b=int(input("       Press 1 for Harry and 2 for satyansh"))
    retrive(b)
input()
