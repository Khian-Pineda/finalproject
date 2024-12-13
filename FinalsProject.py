#FINALS PROJECT ITCS102
#BY KHIAN MHARC L PINEDA
import os
tuloy = True
while tuloy == True:
    print("\n======================================================================================\nCode_Challenge1 --- 1 \tCode_Challenge11 --- 11 \tActivity1 --- 101 \nCode_Challenge2 --- 2 \tCode_Challenge12 --- 12 \tActivity2 --- 102 \nCode_Challenge3 --- 3 \tCode_Challenge13 --- 13 \tActivity3 --- 103 \nCode_Challenge4 --- 4 \tCode_Challenge14 --- 14 \tActivity4 --- 104 \nCode_Challenge5 --- 5 \tCode_Challenge15 --- 15 \tActivity5 --- 105 \nCode_Challenge6 --- 6 \tCode_Challenge16 --- 16 \tAvtivity6 --- 106 \nCode_Challenge7 --- 7 \t\t\t\t\tActivity7 --- 107 \nCode_Challenge8 --- 8 \t\t\t\t\tActivity8 --- 108 \nCode_Challenge9 --- 9 \t\t\t\t\tActivity9 --- 109 \nCode_Challenge10 -- 10 \t\t\t\t\tActivity8 --- 110 \n======================================================================================")
    a = int(input("\nCHOOSE ONLY ONE CHALLENGE U WANT TO OPEN (TYPE ONLY THE NUMBER): ")) 
    if a == 101:
        os.system("cls")

        def Activity101(Activity101):
          print("Hello World")
        Activity101(Activity101)
        continue
    elif a == 102:
        os.system("cls")

        def Activity102(Activity102):
            name = input( "Please enter a name -----> " )
            print ( "Hi!" + name )
        Activity102(Activity102)
        continue

    elif a == 103:
        os.system("cls")
        def Activity103():
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
        Activity103()
        continue
    
    elif a == 104:
        os.system("cls")
        def Activity104():
            number1 = eval (input("enter a number--->" ))
            number2 = eval (input("enter another number--->" ))
            answer = (number1 + number2)

            print("The sum of", number1 ,"and",number2,"is",answer)
        Activity104()
        continue

    elif a == 105:    
        os.system("cls")
        def Activity105():
         
            grade = eval(input("Enter your grade"))
            if grade >= 75-80:
                print("congratulations you just passed the subject")
            else:
                print("bawi nalang next life")
        Activity105()
        continue
    
    elif a == 106:    
        os.system("cls")
        def Activity106():

            x = 5
            print(x)
            x = x + 10
            print(x)
            x = x +15
            print(x)
            x += 10 
            print(x)
            x +=20
            print(x)
        Activity106()
        continue

    elif a == 107:    
        os.system("cls")
        def Activity107():

            gold = 0

            name=input('Hi, enter your name:  ')
            hasMine=input('Did you mine gold today?  ')

            if hasMine.lower() == "yes":
                gold +=1
                print(f'Hi! {name}, Today you have a total of {gold} gold')
            else:
                print(f'Hi! {name}, Today you have a total of {gold} gold')
        Activity107()
        continue

    elif a == 108:    
        os.system("cls")
        def Activity108():

            password = input('Enter your password---> ')

            if password.lower() == "khian" :
                print('Access Granted!!!!')
                print('Enjoy using the system')

            elif password.lower() =='pineda':
                print('Access Granted!!!!')
                print('Enjoy using the system')
            else:
                print('Access Denied!!!!!')
            print('Thank you for using the system')
        Activity108()
        continue

    elif a == 109:
        os.system("cls")
        def Activity109():
        
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
        Activity109()
        continue
    
    elif a == 110:
        os.system("cls")
        def Activity110():
            isDLL= input('Are you a current student of DLL (yes/no):  ')

            if isDLL.lower() == 'yes':
                print('Welcome to the DLL BSIT Scholarship form')
                isiyam= input('Are you from Barangay Ilayang iyam (yes/ no):  ')

                if isiyam.lower() == 'yes':
                    print('Please fillup the second form')
                    isneed=input('What is your current level right now in DLL\nF - Freshmen\nS - Sophomore\nJ - Junior\nR - Senior\nPlease input your answer:  ')
                    if isneed.lower() == 'f':
                        print('Hi Freshmen')
                    elif isneed.lower() == 's':
                        print('Hi Sophomore')
                    elif isneed.lower() == 'j':
                        print('Hi Junior')
                    elif isneed.lower() == 'r':
                        print('Hi Senior')
                    else:
                        print('Invalid choice')
                    isNeeded = input('Do you need this scholarship (yes/no):  ')
                
                    if isNeeded.lower() == 'yes':
                        print('Scholarship Granted')
                    else:
                        print('Thanks for stopping by')
                else:
                    print('Sorry, this Scholarship grant are only for resident of Ilayang iyam')

            else:
                print('Thanks for stopping by')
        Activity110()
        continue
    elif a == 111:
        os.system("cls")
        def Activity111():
            for me in range (1 , 101):
                print(me, 'GOODBYE WORLD')
        Activity111()
        continue
    elif a == 121:
        os.system("cls")
        def Activity121():

            for cycle in range (10,0,-1):
                print(cycle)
        Activity121()
        continue
    
    elif a == 130:
        os.system("cls")
        def Activity130():
            sum = 1
            num=int(input('Enter a number: '))

            for x in range (num,0,-1):
                sum *= x
            print(f"The factorial of {num} is {sum}")
        Activity130()
        continue

    elif a == 140:
        os.system("cls")
        def Activity140():
                
            for x in range ( 0, 11,):
                print(x,end =" ")
                for y in range (0, 11):
                    print("*",end = " ")
                print("")
        Activity140()
        continue

    elif a == 150:
        os.system("cls")
        def Activity15():
                import os

                isContinue = True
                no = 0
                while isContinue == True:
                    ask = input("Would you like to add another triangle (yes / no )--> ")

                    if ask.lower() == "no":
                        print("PROGRAM TERMINATED")
                        break
                        isContinue = False
                    elif ask.lower() == "yes":
                        os.system('cls')
                        no += 1
                        for x in range (1, 6):
                            for r in range (1 , no + 1):
                                for y in range (1 , x + 1):
                                    print("*", end=" ")
                                for z in range (6, x, -1):
                                    print(" ",end=" ")
                            print()
                    else:
                        print("INVALID ANSWER it's only (yes/no)")
                        continue
        Activity15()
        continue

    elif a == 160:
        os.system("cls")
        def Activity160():
        
            for x in range (1,11,):
                for y in range (1, x + 1):
                    print(" ",end=" ")
                for z in range(11, x, -1):
                    print(" * ",end=" ")
                print()
        Activity160()
        continue
    
    elif a == 170:
        os.system("cls")
        def Activity170():
                col = eval(input("Enter number of columns---> "))


                for x in range (1, 11):
                    for y in range (1, col + 1):
                        print(f"{x} x {y} = {x*y}" ,end="\t")
                print()
        Activity170()
        continue
    
    elif a == 180:
        os.system("cls")
        def Activity180():

            tri = eval(input("Enter a number of triangle---> "))

            for x in range (1, 6):
                for r in range (1 , tri + 1):
                    for y in range (1 , x + 1):
                        print("*", end=" ")
                    for z in range (6, x, -1):
                        print(" ",end=" ")
                print()
        Activity180()
        continue
    
    elif a == 190:
        os.system("cls")
        def Activity190():
            tuloy = True
            while tuloy == True:
                name = input("Enter your name: ")
                if name.lower()== "stop":
                    print("PROGRAM TERMINATED")
                    break
                    tuloy = False
                else:
                    continue
        Activity190()
        continue

    elif a == 120:
        os.system("cls")
        def Activity120():
            import os

            isContinue = True
            no = 0
            while isContinue == True:
                ask = input("Would you like to add another triangle (yes / no )--> ")

                if ask.lower() == "no":
                    print("PROGRAM TERMINATED")
                    break
                    isContinue = False
                else:
                    os.system('cls')
                    no += 1
                    for x in range (1, 6):
                        for r in range (1 , no + 1):
                            for y in range (1 , x + 1):
                                print("*", end=" ")
                            for z in range (6, x, -1):
                                print(" ",end=" ")
                        print()
                    continue
        Activity120()
        continue
    
    elif a == 121:
        os.system("cls")
        def Activity21():
            def pang_hi():
                print("HI IT1C")

            def pang_hi_v2(name):
                print(f"Hello {name}")

            def termi():
                print("PROGRAM TERMINATED")

            def activity_2():
                number1 = eval (input("enter a number--->" ))
                number2 = eval (input("enter another number--->" ))
                answer = (number1 + number2)
                print(f"The sum of {number1} and {number2} is {answer}")

            tuloy =  True
            while tuloy == True:
                ask = input("Enter a name---> ")

                if ask.lower() != "stop":
                    pang_hi_v2(ask)
                    if ask == "2":
                        activity_2()
                        continue
                else:
                    termi()
                    break
        Activity21()
        continue
    
    elif a == 1:
        os.system("cls")
        def code_challenge1():
            print("\t\t\t\t\t\t\t\t\b*\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b\b\b*********\n\t\t\t\t\t\t\t\t\b\b\b\b*******\n\t\t\t\t\t\t\t\t\b\b\b*****\n\t\t\t\t\t\t\t\t\b\b***\n\t\t\t\t\t\t\t\t\b*")
        code_challenge1()
        continue

    elif a == 2:
        os.system("cls")
        def code_challenge2():
            name = input("please enter your name ---->")

            print("\n\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\b\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b\b\b\b * *|" + name + "|* *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b\b\b* * * * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\b* * *\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t *")
        code_challenge2()
        continue

    elif a == 3:
        os.system("cls")
        def code_challenge3():
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
        code_challenge3()
        continue

    elif a == 4:
        os.system("cls")
        def code_challenge4():   
            no1 = eval(input("choose a number---> "))
            no2 = eval(input("choose another number ----> "))
            ans1 = (no1 + no2)
            ans2 = (no1 - no2)
            ans3 = (no1 * no2)
            ans4 = (no1 / no2)
            ans5 = (no1 % no2)
            ans6 = (no1 ** no2)
            ans7 = (no1 // no2)

            print("the sum of", no1 ,"and", no2 ,"is", ans1 ,)
            print("the difference of", no1 ," and", no2 ,"is", ans2 ,)
            print("the product of", no1 ,"and", no2 ,"is", ans3 ,)
            print("the qoutient of", no1 ,"and", no2 ,"is", ans4 ,)
            print("the remainder of", no1 ,"and", no2 ,"is", ans5 ,)
            print("the exponent of", no1 ,"and", no2 ,"is", ans6 ,)
            print("the floor division of", no1 ,"and", no2 ,"is", ans7 ,)
        code_challenge4

    elif a == 5:
        os.system("cls")
        def code_challenge5():
            name=input('enter your name:')
            amount=eval(input('enter amount to deposits:'))
            print('------------------------------------------------------------')

            a1=amount//1000
            a2=amount%1000

            b1=a2//500
            b2=a2%500

            c1=b2//200
            c2=b2%200

            d1=c2//100
            d2=c2%100

            e1=d2//50
            e2=d2%50

            f1=e2//20
            f2=e2%20

            g1=f2//10
            g2=f2%10

            h1=g2//5
            h2=g2%5

            i1=h2//1
            i2=h2%1

            print(f'Hi!{name} dreakdown of your deposit is:')
            print(a1,'-- 1000php')
            print(b1,'--- 500php')
            print(c1,'--- 200php')
            print(d1,'--- 100php')
            print(e1,'---- 50php')
            print(f1,'---- 20php')
            print(g1,'---- 10php')
            print(h1,'----- 5php')
            print(i1,'----- 1php')
        code_challenge5()
        continue

    elif a == 6:
        os.system("cls")
        def code_challenge6():

            prelim=eval(input('Enter your grade in prelim :'))
            midterm=eval(input('Enter your grade in midterm :'))
            semifinal=eval(input('Enter your grade in semifinal :'))
            final=eval(input('Enter your grade in final :'))
            quiz=eval(input('Enter your grade in quiz :'))
            proj=eval(input('Enter your grade in project :'))

            grade =(prelim * .15) + (midterm * .15) + (semifinal * .15) + (final * .15) + (quiz * .25) + (proj * .15)

            if grade >100:
                print('YOUR GRADE HAS EXCEEDED MAXIMUM VALUE') 

            elif grade >= 75:
                print('CONGRATULATONS, YOU PASSED WITH AN AVERAGE GRADE OF',grade,)

            else:
                print('SORRY YOU FAILED')
                print(f'your average is {grade}')
        code_challenge6()
        continue
    
    elif a == 7:
        os.system("cls")
        def code_challenge7():
            A = input("DID YOU BUY A MEAT GOOD/s (yes/no)? ")
            if A.upper() == "YES":
                print('\nTHIS ARE THE LIST OF AVAILABLE MEAT GOODS')
                print('===========================================')
                print('Pork ------- 300php/kilo')
                print('Chicken ---- 250php/kilo')
                print('Beef ------- 400php/kilo')
                print('Rabbit ----- 250php/kilo')
                print('Tocino ----- 100php/kilo')
                print('Bacon ------ 120php/kilo')
                print('Bologna -----100php/kilo')
                quan1= eval(input("\nHow many kilos of Pork meat you want to buy? "))
                pork=quan1 * 300

                quan2= eval(input("\nHow many kilos of Chicken meat you want to buy? "))
                chicken=quan2 * 250

                quan3= eval(input("\nHow many kilos of Beef meat you want to buy? "))
                beef=quan3 * 400

                quan4= eval(input("\nHow many kilos of Rabbit meat you want to buy? "))
                rabbit=quan4 * 250

                quan5= eval(input("\nHow many kilos of Tocino meat you want to buy? "))
                tocino=quan5 * 100

                quan6= eval(input("\nHow many kilos of Bacon meat you want to buy? "))
                bacon=quan6 * 120

                quan7= eval(input("\nHow many kilos of Bologna meat you want to buy? "))
                bologna=quan7 * 100

                total= pork+chicken+beef+rabbit+tocino+bacon+bologna
                tax=(pork*0.123) or (chicken*0.123) or (beef*0.123) or (rabbit*0.123) or (tocino*0.123) or (bacon*0.123) or (bologna*0.123)
                total_and_tax= (total + tax)
                print()
                age = input("Are you a Senior Citizen(yes/no)? ")
                if age.lower() =='yes':
                    disc=round(total*0.052)
                    print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat\nwith the total price of {total}php plus a 12.3% tax ({tax}php) and with a discount of 5.2% ({disc}php)")
                
                else:
                    disc=0
                    print(f"Hi, customer, you purhased a \n{quan1}kilo of Pork meat\n{quan2}kilo of Chicken meat\n{quan3}kilo of Beef meat\n{quan4}kilo of Rabbit meat\n{quan5}kilo of Tocino meat\n{quan6}kilo of Bacon meat\n{quan7}kilo of Bologna meat with the total price of {total}php plus a 12.3% tax(",tax,")")
                print()
                E = float(input("Amount Given: "))
                print()
                if E>= total_and_tax:
                    change = round(E - total_and_tax + disc)
                    print('=================RECEIPT===================')
                    print('Qty.    Description           Amount')
                    print(f'{quan1}x ----- PORK MEAT.........{pork}php')
                    print(f'{quan2}x ----- CHICKEN MEAT......{chicken}php')
                    print(f'{quan3}x ----- BEEF MEAT.........{beef}php ')
                    print(f'{quan4}x ----- RABBIT MEAT.......{rabbit}php')
                    print(f'{quan5}x ----- TOCINO MEAT.......{tocino}php')
                    print(f'{quan6}x ----- BACON MEAT........{bacon}php')
                    print(f'{quan7}x ----- BOLOGNA MEAT......{bologna}php')
                    print()
                    print(f'SUBTOTAL...................{total}php')
                    print(f'TAX(12.3%).................{tax}php')
                    print(f'TOTAL......................{total_and_tax}php')
                    print(f'PAY AMOUNT.................{E}php')
                    print(f'DISCOUNT(5.2%).............{disc}php') 
                    print(f'CHANGE.....................{change}php')
                    print()
                    print("==THANK YOU COME AGAIN!!==")
                else:
                    E< total_and_tax
                    print("Insufficient Amount")
            else :
                print("Thankyou for stopping by!")
        code_challenge7()
        continue

    elif a == 8:
        os.system("cls")
        def code_challenge8():
            sum = 0
            odd = 0
            even = 0
            for x in range (1,11):
                num=int(input(f'enter number {x}: '))
                sum += num
                if num % 2 == 0:
                    odd += num
                else:
                    even += num


            print(f'The sum of all numbers given is {sum}')
            print(f'The odd of all numbers given is {odd}')
            print(f'The even of all numbers given is {even}')
        code_challenge8()
        continue
    
    elif a == 9:
        os.system("cls")
        def code_challenge9():
            for x in range(1,6):
                p=1
                for y in range(1, x + 1):
                    print("  ", end = " ")
                for z in range(6, x, -1):
                    print(p,end="  ")
                    p+=1
                print()
        code_challenge9()
        continue

    elif a == 10:
        os.system("cls")
        def code_challenge10():

            for x in range(6,1,-1):
                for a in range(x,1,-1):
                    print(" ",end="   ")
                for b in range(x,6,1):
                    print("*  ",end=" ")
                for b in range(x,6,1):
                    print("*  ",end=" ")
                print()

            for x in range(1,6):
                for a in range(1,x,1):
                    print(" ",end="   ")
                for b in range(6,x,-1):
                    print("*  ",end=" ")
                for b in range(6,x,-1):
                    print("*  ",end=" ")
                print()
        code_challenge10()
        continue

    elif a == 11:
        os.system("cls")
        def code_challenge11():

            for x in range(6,1,-1):
                for a in range(x,1,-1):
                    print(" ",end="   ")
                for b in range(x,7,1):
                    print("*  ",end=" ")
                for b in range(x,6,1):
                    print("*  ",end=" ")
                print()

            for x in range(1,7):
                for a in range(1,x,1):
                    print(" ",end="   ")
                for b in range(7,x,-1):
                    print("*  ",end=" ")
                for b in range(6,x,-1):
                    print("*  ",end=" ")
                print()
        code_challenge11()
        continue
    
    elif a == 12:
        os.system("cls")
        def code_challenge12():

            for x in range (6,1,-1):
                for y in range(1,x+1):
                    print(" ", end = " ")
                for z in range(7,x,-1):
                    print("*",end=" ")
                for a in range(6,x,-1):
                    print("*",end=" ")
                print()

            for x in range (1,6):
                for y in range(1,6):
                    print(" ", end = " ")
                for a in range(1,4):
                    print("*", end = " ")
                print()
        code_challenge12()
        continue

    elif a == 13:
        os.system("cls")
        def code_challenge13():
            for x in range (6,1,-1):
                for y in range (1, x + 1):
                    print(" ",end=" ")
                for z in range(6, x, -1):
                    print("*",end=" ")
                for a in range(5, x, -1):
                    print("*",end=" ")
                print()
                
            for x in range (1,6):
                for y in range (1, x + 1):
                    print(" ",end=" ")
                for z in range(5, x, -1):
                    print("*",end=" ")
                for xx in range(6, x, -1):
                    print("*",end=" ")
                print()
        code_challenge13()
        continue

    elif a == 14:
        os.system("cls")
        def code_challenge14():
            tuloy = True
            a = 0
            while tuloy == True:
                number = eval(input("Enter a number--->  "))
                if number == 0:
                    print("Program Terminated")
                    print(f"The total of the number you enter is {a}")
                    break
                else:
                    a += number
                    continue
        code_challenge14()
        continue

    elif a == 15:
        os.system("cls")
        def code_challenge15():
            import os
            t = 1
            A = True

            while A == True:
                B = input("Would you like to add a triangle? (yes / no)----> ")
                if B.lower() == "yes":
                    os.system("cls")
                    t += 1
                    for x in range(1, 6):
                        for r in range(1, t):
                            for y in range(1, x +1):
                                print("*", end=" ")
                            for z in range(6, x, -1):
                                print(" ", end=" ")
                        print()
                elif B.lower() == "no":
                    os.system("cls")
                    print("Program Terminated.")
                    break
                    A = False
                else:
                    print("Invalid input please answer only with yes or no.")
                    continue
        code_challenge15()
        continue

    elif a == 16:
        os.system("cls")
        def code_challenge16():
            def denomination(amount):
                    print("\nDenomination Breakdown:")
                    A = amount // 1000
                    AA = amount % 1000

                    B = AA // 500
                    BB = AA % 500

                    C = BB // 200
                    CC = BB % 200

                    D = CC // 100
                    DD = CC % 100

                    E = DD // 50
                    EE = DD % 50

                    F = EE // 20
                    FF = EE % 20

                    G = FF // 10
                    GG = FF % 10

                    H = GG // 5
                    HH = GG % 5

                    I = HH // 1

                    print("1000---", A)
                    print("500----", B)
                    print("200----", C)
                    print("100----", D)
                    print("50-----", E)
                    print("20-----", F)
                    print("10-----", G)
                    print("5------", H)
                    print("1------", I)
            accounts = {}
            def create_account():
                    username = input("Enter a username: ")
                    if username in accounts:
                        print("Account already exists!")
                    else:
                        accounts[username] = 0
                        print(f"Account created successfully for {username}.")
            def deposit():
                    username = input("Enter your username: ")
                    if username in accounts:
                        try:
                            amount = int(input("Enter amount to deposit : "))
                            if amount > 0:
                                accounts[username] += amount
                                print(f"Deposited {amount} successfully. New balance: {accounts[username]}")
                                denomination(amount)
                            else:
                                print("Amount must be positive!")
                        except ValueError:
                            print("Invalid input! Please enter a whole number.")
                    else:
                        print("Account not found!")
            def withdrawal():
                    username = input("Enter your username: ")
                    if username in accounts:
                        try:
                            amount = int(input("Enter amount to withdraw (whole numbers only): "))
                            if 0 < amount <= accounts[username]:
                                accounts[username] -= amount
                                print(f"Withdrawn {amount} successfully. Remaining balance: {accounts[username]}")
                                denomination(amount)
                            else:
                                print("Insufficient funds or invalid amount!")
                        except ValueError:
                            print("Invalid input! Please enter a whole number.")
                    else:
                        print("Account not found!")
            def check_balance():
                    username = input("Enter your username: ")
                    if username in accounts:
                        print(f"Your balance: {accounts[username]}")
                    else:
                        print("Account not found!")
            def options():
                    while True:
                        print("\nBanking System")
                        print("1. Create Account")
                        print("2. Deposit")
                        print("3. Withdraw")
                        print("4. Check Balance")
                        print("5. Exit")
                        choice = input("Choose an option (1-5): ")

                        if choice == '1':
                            create_account()
                        elif choice == '2':
                            deposit()
                        elif choice == '3':
                            withdrawal()
                        elif choice == '4':
                            check_balance()
                        elif choice == '5' or "Exit":
                            print("Thank you for using the Banking System!")
                            break
                        else:
                            print("Invalid option. Please try again.")
        code_challenge16()
        continue
