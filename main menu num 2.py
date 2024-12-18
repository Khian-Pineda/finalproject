import os
tuloy = True
while tuloy == True:

    def main_menu():
        os.system("cls")
        print("=====================================")
        print("         Welcome to My Program       ")
        print("=====================================")
        print("1. Activities")
        print("2. Code Challenges")
        print("0. Exit")
        print("=====================================")

    # Activity Menu
    def activity_menu():
        os.system("cls")
        print("=====================================")
        print("             Activity Menu           ")
        print("=====================================")
        print("1. Activity 1")
        print("2. Activity 2")
        print("3. Activity 3")
        print("0. Back to Main Menu")
        print("=====================================")

    # Code Challenge Menu
    def code_challenge_menu():
        os.system("cls")
        print("=====================================")
        print("          Code Challenge Menu       ")
        print("=====================================")
        print("1. Code Challenge 1")
        print("2. Code Challenge 2")
        print("3. Code Challenge 3")
        print("0. Back to Main Menu")
        print("=====================================")

    # Main Program Logic
    def run_program():
        while True:
            main_menu()
            choice = int(input("Choose an option: "))

            if choice == "1":
                while True:
                    activity_menu()  
                    activity_choice = int(input("Choose an activity: "))

                    if activity_choice == "1":
                         print("Hello World")
                    elif activity_choice == "2":
                        name = int(input("Please enter a name -----> "))
                        print("Hi! " + name)
                    elif activity_choice == "3":
                        
                        name = input("Please input your name here ---> ")
                        fname = input("Please input your father's name here ---> ")
                        mname = input("Please input your mother's name here ---> ")
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
                        age = input("Please input your age here ---> ")
                            
                        print("\n\n\n\n\tHello, My name is,", name ,"I'm", age ,"yrs old.\n\tI identify as", gender ,"\n\tMy father's name is", fname ,"\n\tMy mother's name is", mname ,"\n\tMy Birthday is in", birthmonth , birthdate , birthyear ,"\n\tI live in", address,"\n\tI am", maritalstatus ,"\n\tI am", ethnicity ,"Citizen\n\tMy mobile number is:", mobile ,"\n\tYou may contact me at my email:", email ,"\n\tThank You!!!\n\n\n")
                    elif activity_choice == "0":
                        break 
                    else:
                        print("Invalid choice, please try again.")

            elif choice == "2":
              
                while True:
                    code_challenge_menu()  
                    code_choice = input("Choose a code challenge: ")
                    if code_choice == "1":
                        print("Code Challenge 1: Not Implemented Yet.")  # Example, you can add your logic
                    elif code_choice == "2":
                        print("Code Challenge 2: Not Implemented Yet.")
                    elif code_choice == "3":
                        print("Code Challenge 3: Not Implemented Yet.")
                    elif code_choice == "0":
                        break
                    else:
                        print("Invalid choice, please try again.")

            elif choice == "0":
                print("Exiting the program...")  # Exit the program
                break
            else:
                print("Invalid choice, please try again.")
