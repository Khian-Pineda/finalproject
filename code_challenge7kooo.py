name = input("Your name: ")
grocery = input("Do you want to buy? (yes or no): ")
if grocery.lower() == 'yes':
	print("\nTHIS IS OUR PRODUCTS:\n1. HOT DOG - $100\n2. CORN DOG - $120\n3. CHEESY DOG - $150")

	quanti = eval(input("\nHow many HOT DOG you want to buy? "))
	prc = (quanti * 100)
	
	quanti2 = eval(input("\nHow many CORN DOG you want to buy? "))
	prc2 = (quanti2 * 120)
	
	quanti3 = eval(input("\nHow many CHEESY DOG you want to buy? "))
	prc3 = (quanti3 * 150)
	
	total = prc + prc2 + prc3
	tax = round(total * 0.123)
	ttax = round(total + tax)

	id = input("\nDo you have Senior/Student/PWD ID? (yes or no): ")
	if id.lower() == 'yes': 
		discount = round(ttax * 0.052)
	else: 	
		discount = 0

	print(f"\nGood day {name}!, you ordered {quanti}pcs of HOT DOG, {quanti2}pcs of CORN DOG and {quanti3}pcs of CHEESY DOG with a price of ${total} with 12.3% of tax with a total of ${ttax}.")
			
	money = eval(input("\nPlease type the amount you'll give: $"))
	if money >= ttax:
		change = round(money - ttax + discount)
		print(f"\n\t\t\t==RECEIPT== \nQty.    Description           Amount\n{quanti}x ---- HOT DOG (100) ------- ${prc} \n{quanti2}x ---- CORN DOG (120) ------ ${prc2} \n{quanti3}x ---- CHEESY DOG (150) ---- ${prc3} \n\tSUBTOTAL ------------ ${total} \n\tSALES TAX (12.3%) --- ${tax} \n\tTOTAL --------------- ${ttax} \n\tPAY AMOUNT ---------- ${money}\n\tDISCOUNT (5.2%) ----- ${discount} \n\tCHANGE -------------- ${change} \n\t\t ==THANK YOU FOR SHOPPING!==")
	else:
		money<= ttax
		print("insufficient amount, please try again.")

		
else: 
	print("\noki.")