def getdata():
    import datetime
    x=datetime.datetime.now()
    return x

print('Press 1:to add data .  \nPress 2 : to retrieve data.\n')
choice=int(input('Enter No. of your choice :: '))
if choice==1:
    print('\nPress 1:for Rohan.\nPress 2: for Rahul.\n Press 3: for Raj.\n')
    a=int(input('Enter your choice :: '))
    if a==1:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            rohan=open("Rohan diet.txt","a")
            eat=input('\nWrite your eating schedule.\n')
            rohan.write(str("\nAt this  "+  str(getdata()) +  " rohan ate " + eat+"\n"))
            rohan.close()
        elif sch==2:
            rohan=open("Rohan exercise.txt","a")
            exer=input('\nWrite your exercise schedule.\n')
            rohan.write(str("\nAt this  "+ str(getdata())+ " rohan exercised " + exer+"\n"))
            rohan.close()
    elif a==2:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            rahul=open("Rahul diet.txt","a")
            eat=input('\nWrite your eating schedule.\n')
            rahul.write(str("\nAt this  " +str(getdata())+ " rahul ate " + eat+"\n"))
            rahul.close()
        elif sch==2:
            rahul=open("Rahul exercise.txt","a")
            exer=input('\nWrite your exercise schedule.\n')
            rahul.write(str("\nAt this " + str(getdata())+ " rahul exercised " + exer+"\n"))
            rahul.close()
    elif a==3:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            raj=open("Raj diet.txt","a")
            eat=input('\nWrite your eating schedule.\n')
            raj.write(str("\nAt this " +str(getdata())+ " raj ate " + eat+"\n"))
            raj.close()
        elif sch==2:
            raj=open("Raj exercise.txt","a")
            exer=input('\nWrite your exercise schedule.\n')
            raj.write(str("\nAt this " +str(getdata())+ " raj exercised " + exer+"\n"))
            raj.close()

if choice==2:
    print('\nPress 1:for Rohan.\nPress 2: for Rahul.\n Press 3: for Raj.\n')
    a=int(input('Enter your choice :: '))
    if a==1:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            rohan=open("Rohan diet.txt","r")
            b=rohan.read()
            print(b)
            rohan.close()
        elif sch==2:
            rohan=open("Rohan exercise.txt","r")
            print(rohan.read())
            rohan.close()
    elif a==2:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            rahul=open("Rahul diet.txt","r")
            print(rahul.read())
            rahul.cloahul
        elif sch==2:
            rahul=open("Rahul exercise.txt","r")
            print(rahul.read())
            rahul.close()
    elif a==3:
        print('\nPress 1: diet schedule. \nPress 2: Exercise schedule.\n ')
        sch=int(input('Enter your choice :: '))
        if sch==1:
            raj=open("Raj diet.txt","r")
            print(raj.read())
            raj.close()
        elif sch==2:
            raj=open("Raj exercise.txt","r")
            print(raj.read())
            raj.close()
            