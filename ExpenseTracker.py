print('<<<<Welcome to semicolon Expenses Tracker App>>>>')

checkout = []

def display_menu():
	return (
	"\n<<<<<<<<<Welcome to the menu>>>>>>>>\n"
	"1.Add an expense\n"
	"2.View all expenses\n"
	"3.Calculate total expenses\n"
	"4.Exit"

	)

def add_expense(date,name,amount):

	checkout.append({'name': name, 'amount': amount, 'date': date})
	return"Expenses added.... "



def view_expense():

	if not checkout:
		return "You haven't purchase anything yet!! "
	else:
		expenses_cont = "All Expenses:\n"
		for expense in checkout:
				expenses_list += f"Goods: {expense['name']} , Amount: {expense['amount']} , Date: {expense['date']}\n"
		return expenses_Cont


def calculate_expenses():
	if not checkout:
		return "Total Expenses: 0"
	total = sum(expense['amount'] for expense in checkout)
	return f"Total Expenses: {total}"
	
	




	

def main():
	while True:
		menu = display_menu()
		print(menu)
		option = input('pick ur preferable order(1_4): ')
		

		if option == '1':
			date = input('Enter date (YYYY_MM_DD): ')
			name = input('Enter goods bought: ')

			while True:
				amount = float(input('Enter amount of goods: '))

				if amount < 1:
					print('enter a positive amount')
				else:
					
					result = add_expense(date, name, amount)
					print(result)
					break

	
		elif option == '2':
			result = view_expense()
			print(result)
		elif option == '3':
			result = calculate_expenses()
			print(result)
		
		elif option == '4':
			print('Good bye thanks😭!!')
			break
		else:
		   print('Invalid number')
		
if __name__ == "__main__":


    main()

