print('<<<<Welcome to semicolon Expenses Tracker App>>>>')

checkout = []

def display_menu():
	print('Welcome to the menu')
	print('1.Add an expense')
	print('2.View all expenses')
	print('3.Calculate total expenses')
	print('4.Exit')

def add_expense():

	date = input('Enter date(YY_MM_DD): ')
	name = input('Enter goods bought: ')
	amount = float(input('Enter amount of goods: '))
	checkout.append({'name': name, 'amount': amount})
	print("expenses added.... ")



def view_expense():

	if not checkout:
		print("You haven't purchase anything yet!!/n ")
	else:
		print('All espenses/n')
		for expense in checkout:
				print(f"Checkouts: {expense['name']} , Amount: {expense['amount']}")




	

def main():
	while True:
		display_menu()
		option = input('pick ur preferable order(1_4): ')

		if option == '1':
			add_expense()
	
		if option == '2':
			view_expense()


if __name__ == "__main__":
    main()