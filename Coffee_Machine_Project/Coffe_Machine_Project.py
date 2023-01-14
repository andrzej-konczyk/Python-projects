"""This code defines a menu of coffee options with their corresponding ingredients and costs, as well as a
 dictionary for the resources available to the coffee machine. It also defines several global variables for
 tracking the state of the machine, such as the amount of money deposited, whether a transaction or refund has
 been completed, and whether a question about the next transaction has been asked.

 The code includes several functions, including:

 1.print_report() which prints a report of the coffee machine's resources and the last deposit.
 2.check_resources(coffee_type) which checks if the resources are sufficient for the selected type of coffee and
 returns a boolean value.
 3.another_transaction() which prompts the user if they would like to proceed with another transaction and
 returns a boolean value.
 4. coin_process(coffee_type) which prompts the user to insert coins and verifies if the
 amount deposited is sufficient to purchase the selected type of coffee. If the amount is not sufficient,
 it gives the user the option to refund or deposit the coins.
 5. make_coffee(coffee_type) which makes the selected type of coffee if the resources are sufficient and the amount
 deposited is sufficient. The code also includes a main loop which prompts the user to select a type of coffee and
 calls the appropriate functions to process the
 transaction."""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


money = 0
last_change = 0
transaction_done = False
refund_done = False
next_question_asked = False
exit_coffee_machine = False


def print_report():
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n"
          f"Deposit: ${last_change}")
    return


def check_resources(coffee_type):
    if MENU[coffee_type]['ingredients']['water'] > resources['water']:
        print('Sorry there is not enough water')
        return False
    elif MENU[coffee_type]['ingredients']['milk'] > resources['milk']:
        print('Sorry there is not enough milk')
        return False
    elif MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry there is not enough coffee')
        return False
    else:
        return True


def another_transaction():
    global next_question_asked
    global transaction_done
    global refund_done
    global exit_coffee_machine
    if transaction_done or refund_done or next_question_asked:
        return False
    else:
        next_question_asked = True
        next_coffee = input('Do you would like to proceed with next transaction? (Yes/No): ')
        if next_coffee == 'Yes':
            next_question_asked = False
            transaction_done = False
            refund_done = False
            return True
        elif next_coffee == 'No':
            transaction_done = True
            exit_coffee_machine = True
            refund_done = False
            return False


def coin_process(coffee_type):
    global last_change
    global transaction_done
    global refund_done
    global exit_coffee_machine
    if check_resources(coffee_type):
        print(f"You selected {coffee_type} and it costs {MENU[coffee_type]['cost']}$")
        print(f"Current deposit: ${round(last_change,2)}")
        print('Please insert coins.')
        quarters = input('How many quarters?: ') or 0
        dims = input('How many dimes?: ') or 0
        nickles = input('How many nickles?: ') or 0
        pennies = input('How many pennies?: ') or 0
        paid_money = (float(quarters) * 0.25 + float(dims) * 0.1 + float(nickles) * 0.05 + float(pennies) * 0.01
                      + last_change)
        more = round(MENU[coffee_type]["cost"] - paid_money, 2)
        if paid_money < MENU[coffee_type]['cost']:
            print(f'Sorry, not enough money. You need {more}$ more')
            if not exit_coffee_machine:
                action = input('Do you want to refund or deposit the coins? (refund/deposit): ')
                if action == 'refund':
                    last_change = 0
                    refund_done = True
                    transaction_done = False
                elif action == 'deposit':
                    print('Coins deposited, please make your choice again')
                    last_change = paid_money
                    transaction_done = False
                    refund_done = True
            else:
                return
        else:
            print(f"That is your {coffee_type} ☕. Enjoy!")
            last_change = round(paid_money - MENU[coffee_type]['cost'], 2)
            resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
            transaction_done = True
            return another_transaction()
    elif not check_resources(coffee_type):
        print("Transaction failed")
        return another_transaction()


def coffee_machine():
    next_operation = True
    while next_operation:
        coffee_type = input('What would you like (espresso/latte/cappuccino): ')
        if coffee_type == 'report':
            print_report()
        else:
            enough_resources = check_resources(coffee_type)
            if enough_resources:
                if coin_process(coffee_type):
                    next_coffee = input('Do you would like to proceed with next transaction? (Yes/No): ')
                    if next_coffee == 'No':
                        print(f"Your change is {last_change}")
                        break
            else:
                print('Transaction failed')
            next_coffee = input('Do you would like to proceed with next transaction? (Yes/No): ')
            if next_coffee == 'No':
                print('Thank you and have a good day! Your coins are refunded')
                break
            else:
                if next_coffee == 'No':
                    print('Thank you and have a good day! Your coins are refunded')
                    break


coffee_machine()
