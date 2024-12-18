def body():
    while True:
        print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
        print(f"Bachelor Of Science In Infomation Technology - 1C")
        print(f"\nPlease Select an Option:   ")
        print(f"\n1. Open Activity Folder")  
        print(f"2. Open Code Challenge Folder")
        print(f"3. Exit Program")

        menu = input(f"\nChoose what action you want to do:  ")
            
        if menu == "1":
            os.system("cls")
            def act_folder1():
                print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
                print(f"Bachelor Of Science In Infomation Technology - 1C")
                print(f"Activity 1")
                print(f"Activity 2")
                print(f"Activity 3")
                print(f"Activity 4")
                print(f"Activity 5")
                print(f"Activity 6")
                print(f"Activity 7")
                print(f"Activity 8")
                print(f"Activity 9")
                print(f"Activity 10")
                print(f"Activity 12")
                print(f"Activity 13")
                print(f"Activity 13")
                print(f"Activity 14")
                print(f"Activity 15")
                print(f"Activity 16")
                print(f"Activity 17")
                print(f"Activity 18")
                print(f"Activity 19")
                print(f"Activity 20")
                print(f"Activity 21")
                print(f"Activity 22")
                print(f"Activity 23")
                print(f"Activity 24")
                print(f"Activity 25")
                print(f"Type 'back' to back to menu")
                tuloy = True
                while tuloy == True:
                    piliact = input(f"Choose the number of activity you wish to open--->  ")
                    if piliact =="1":
                        act_1()
                    elif piliact =="2":
                        act_2()
                    elif piliact =="3":
                        act_3()
                    elif piliact =="4":
                        act_4()
                    elif piliact =="5":
                        act_5()
                    elif piliact =="6":
                        act_6()
                    elif piliact =="7":
                        act_7()
                    elif piliact =="8":
                        act_8()
                    elif piliact =="9":
                        act_9()
                    elif piliact =="10":
                        act_10()
                    elif piliact =="11":
                        act_11()
                    elif piliact =="12":
                        act_12()
                    elif piliact =="13":
                        act_13()
                    elif piliact =="14":
                        act_14()
                    elif piliact =="15":
                        act_15()
                    elif piliact =="16":
                        act_16()
                    elif piliact =="17":
                        act_17()
                    elif piliact =="18":
                        act_18()
                    elif piliact =="19":
                        act_19()
                    elif piliact =="20":
                        act_20()
                    elif piliact =="21":
                        act_21()
                    elif piliact =="22":
                        act_22()
                    elif piliact =="23":
                        act_23()
                    elif piliact =="24":
                        act_24()
                    elif piliact =="25":
                        act_25()
                    elif piliact.lower() =="back":
                        return menu
                    else:
                        print("Invalid Choice, Please try again.")    
                        continue 
                                        
            act_folder1()
            
        elif menu == "2":
            os.system("cls")
            def cc_folder2():
                print(f"\nWelcome to code compilation of Cris Laurence Pelaez")
                print(f"Bachelor Of Science In Infomation Technology - 1C")
                print(f"Code Challenge 1")
                print(f"Code Challenge 2")
                print(f"Code Challenge 3")
                print(f"Code Challenge 4")
                print(f"Code Challenge 5")
                print(f"Code Challenge 6")
                print(f"Code Challenge 7")
                print(f"Code Challenge 8")
                print(f"Code Challenge 9")
                print(f"Code Challenge 10")
                print(f"Code Challenge 11")
                print(f"Code Challenge 12")
                print(f"Code Challenge 13")
                print(f"Code Challenge 14")
                print(f"Code Challenge 15")
                print(f"Code Challenge 16")
                print(f"Type 'back' to back to menu")  
                tuloy = True
                while tuloy == True:
                    pilicc = input(f"Choose the number of activity you wish to open--->  ")
                    if pilicc =="1":
                        cc_1()
                    elif pilicc =="2":
                        cc_2()
                    elif pilicc =="3":
                        cc_3()
                    elif pilicc =="4":
                        cc_4()
                    elif pilicc =="5":
                        cc_5()
                    elif pilicc =="6":
                        cc_6()
                    elif pilicc =="7":
                        cc_7()
                    elif pilicc =="8":
                        cc_8()
                    elif pilicc =="9":
                        cc_9()
                    elif pilicc =="10":
                        cc_10()
                    elif pilicc =="11":
                        cc_11()
                    elif pilicc =="12":
                        cc_12()
                    elif pilicc =="13":
                        cc_13()
                    elif pilicc =="14":
                        cc_14()
                    elif pilicc =="15":
                        cc_15()
                    elif pilicc =="16":
                        cc_16()
                    elif pilicc.lower() =="back":
                        return menu
                    else:
                        print("Invalid Choice, Please try again.")    
                        continue 


            cc_folder2()
                    
     

        elif menu == "3":
            os.system("cls")
            def exit3():
                print(f"\nProgram terminated, Thank you for checking my Program.\n")
            exit3()
            break
        else:
            print("Invalid Choice, Please try again.")    
            continue     
body()