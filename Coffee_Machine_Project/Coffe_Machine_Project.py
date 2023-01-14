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

# Project steps:

# TODO 1.Print report of all coffee machine resources

# TODO 2. Check if resources are sufficient for selected type of coffee

# TODO 3. Process coins step

# TODO 4. Verification if transaction was successful

# TODO 5. Make coffee step


money = 0
last_change = 0


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


def coin_process(coffee_type):
    global last_change
    if check_resources(coffee_type):
        print(f"You selected {coffee_type} and it costs {MENU[coffee_type]['cost']}$")
        print(f"Current deposit: ${last_change}")
        print('Please insert coins.')
        quarters = input('How many quarters?: ') or 0
        dims = input('How many dimes?: ') or 0
        nickles = input('How many nickles?: ') or 0
        pennies = input('How many pennies?: ') or 0
        paid_money = (float(quarters) * 0.25 + float(dims) * 0.1 + float(nickles) * 0.05 + float(pennies) * 0.01 + last_change)
        if paid_money < MENU[coffee_type]['cost']:
            print(f'Sorry, not enough money. You need {MENU[coffee_type]["cost"]-paid_money}$ more')
            return False
        else:
            last_change = round(paid_money - MENU[coffee_type]['cost'], 2)
            resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
            resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
            resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
            return True


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
                    print(f"That is your {coffee_type} ☕. Enjoy!")
                else:
                    print('Transaction failed')
            else:
                print('Transaction failed')
            next_coffee = input('Do you would like to proceed with next transaction? (Yes/No): ')
            if next_coffee == 'No':
                print('Thank you and have a good day!')
                break
            else:
                if next_coffee == 'No':
                    print('Thank you and have a good day!')
                    break


coffee_machine()
