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
	