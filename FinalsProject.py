#FINALS PROJECT ITCS102
#BY KHIAN MHARC L PINEDA
import os
tuloy = True
while tuloy == True:
    print("\n======================================================================================\nCode_Challenge1 --- 1 \tCode_Challenge11 --- 11 \tActivity1 --- 101 \nCode_Challenge2 --- 2 \tCode_Challenge12 --- 12 \tActivity2 --- 102 \nCode_Challenge3 --- 3 \tCode_Challenge13 --- 13 \tActivity3 --- 103 \nCode_Challenge4 --- 4 \tCode_Challenge14 --- 14 \tActivity4 --- 104 \nCode_Challenge5 --- 5 \tCode_Challenge15 --- 15 \tActivity5 --- 105 \nCode_Challenge6 --- 6 \tCode_Challenge16 --- 16\nCode_Challenge7 --- 7 \nCode_Challenge8 --- 8 \nCode_Challenge9 --- 9 \nCode_Challenge10 -- 10")
    a = int(input("\nCHOOSE ONLY ONE CHALLENGE U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
    if a == 1:
        os.system("cls")

        def Activity1(Activity1):
          print("Hello World")
        Activity1(Activity1)
        continue
    elif a == 2:
        os.system("cls")

        def Activity2(Activity2):
            name = input( "Please enter a name -----> " )
            print ( "Hi!" + name )
        Activity2(Activity2)

        def Activity3(Activity3):
            name = input("Please input your name here ---> ")
            fname = input("Please input your fname here ---> ")
            mname = input("Please input your mname here ---> ")
            birthdate = input("Please input your birth date here ---> ")
            birthmonth = input("Please input your birthmonth here ---> ")
            birthyear = input("Please input your birthyear here ---> ")
            maritalstatus = input("Please input your maritalstatus here ---> ")
            religion = input("Please input your religion here ---> ")
            ethnicity = input("Please input your ethnicity here ---> ")
            mobile = input("Please input your mobile here ---> ")
            email = input("Please input your email here ---> ")
            gender = input("Please input your gender here ---> ")
            address = input("Please input your address here ---> ")
            age = input(" Please input your age here ---> ")


            print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Bithday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me in my email:", email ,"\n\tThank You!!!\n\n\n")

def Activity4():
    
    number1 = eval (input("enter a number--->" ))
    number2 = eval (input("enter another number--->" ))
    answer = (number1 + number2)

    print("The sum of", number1 ,"and",number2,"is",answer)
    
def Activity5():
    
    grade = eval(input("Enter your grade"))


    if grade >= 75-80:
        print("congratulations you just passed the subject")
    else:
        print("bawi nalang next life")

    print("bawi nalang next life")

def Activity6():

    x = 5

    print(x)

    x = x + 10

    print(x)

    x = x +15

    print(x)

    x += 10 

    print(x)

    x+=20

    print(x)

def Activity7():

    gold = 0

    name=input('Hi, enter your name:  ')
    hasMine=input('Did you mine gold today?  ')

    if hasMine.lower() == "yes":
        gold +=1
        print(f'Hi! {name}, Today you have a total of {gold} gold')
    else:
        print(f'Hi! {name}, Today you have a total of {gold} gold')

def Activity8():

    password = input('Enter your password---> ')

    if password.lower() == "lester" :
        print('Access Granted!!!!')
        print('Enjoy using the system')

    elif password.lower() =='casipit':
        print('Access Granted!!!!')
        print('Enjoy using the system')
    else:
        print('Access Denied!!!!!')
    print('Thank you for using the system')

def Activity9():
   
    age = eval(input("Enter your age: "))

    if age > 100:
        print("\nyou are an Ancient One")

    elif age >= 60:
        print("\nyou are a Senior Citizen")

    elif age >= 46:	
        print("\nyou are in a Post Adulthood")

    elif age >= 32:
        print("\nyou are in a Mid Adulthood")

    elif age >= 19:
        print("\nyou are in a Early Adulthood")

    elif age >= 14:
        print("\nyou are a Teenager")

    elif age >= 8:
        print("\nyou are a Pre teen")

    elif age >= 1:
        print("\nyou are a Toddler")

    elif age < 1:
        print("\nCondolence ")

def Activity20():
 pass
def Activity20():
 pass
def Activity20():
 pass
def Activity20():
 pass

