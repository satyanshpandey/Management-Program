import datetime
def gettime():
    return datetime.datetime.now()
def take(k):
    if k==1:
        n=int(input("Enter 1 for about video and 2 for learn"))
        if n==1:
            value=input("Type here...")
            with open("pythonVid.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+ "\n")
                print("written successfully...")
        elif n==2:
            value=input("Type here...")
            with open("pythonLearn.txt","a") as op:
                op.write(str([str(gettime())])+":" +value+ "\n")
                print("Written successfully...")
    elif k==2:
        n=int(input("enter 1 for video and topics and enter 2 for tpoics learn by video"))
        if n==1:
            value=input("Type here for video topics...")
            with open("webDevelopment.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+ "\n")
                print("Written successfully")
        elif n==2:
            value=input("Type here for topics is learn by video...")
            with open("web.txt","a") as op:
                op.write(str([str(gettime())])+":" +value+ "\n")
                print("Written successfully")
def retrieve(k):
    if k==1:
        n=int(input("Enter 1 for videoTopics and 2 for topics"))
        if n==1:
            with open("pythonVid.txt") as op:
                for i in op:
                    print(i,end=" ")
        elif n==2:
            with open("pythonLearn.txt") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        n=int(input("Enter 1 for web videos Topics and 2 for web topics"))
        if n==1:
            with open("webDevelopment.txt") as op:
                for i in op:
                    print(i,end="")
        elif n==2:
            with open("web.txt") as op:
                for i in op:
                    print(i,end="")


a=int(input("Press 1 for lock and 2 for retrieve values"))
if a==1:
    b=int(input("Enter 1 for python 2 for web"))
    take(b)
elif a==2:
    b=int(input("Enter 1 for python and 2 for web development"))
    retrieve(b)
