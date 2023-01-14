MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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


def print_report():
    print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${money}")
    return


def check_resources(coffee_type):
    if True:
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
    if check_resources(coffee_type):
        print('Please insert coins.')
        quarters = int(input('How many quarters?: '))
        dims = int(input('How many dimes?: '))
        nickles = int(input('How many nickles?: '))
        pennies = int(input('How many pennies?: '))
        paid_money = (quarters * 0.25 + dims * 0.1 + nickles * 0.05 + pennies * 0.01)
        change = round(paid_money - MENU[coffee_type]['cost'], 2)
        print(f"Here is ${change} in change")
        resources['water'] = resources['water'] - MENU[coffee_type]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[coffee_type]['ingredients']['coffee']
        return


def coffee_machine():
    next_operation = True
    while next_operation:
        coffee_type = input('What would you like (espresso/latte/cappuccino): ')
        if coffee_type == 'report':
            print_report()
        else:
            check_resources(coffee_type)
            coin_process(coffee_type)
            next_coffee = input('Do you would like to proceed with next transaction? (Yes/No): ')
            if next_coffee == 'No':
                print('Thank you and have a good day!')
                break
            else:
                if next_coffee == 'No':
                    print('Thank you and have a good day!')
                    break
                elif next_coffee == 'Yes':
                    coffee_type = input('What would you like (espresso/latte/cappuccino): ')
                    if coffee_type == 'report':
                        print_report()
                    else:
                        check_resources(coffee_type)
                        coin_process(coffee_type)
                        next_operation = input('Do you would like to proceed with next transaction? (Yes/No): ')


coffee_machine()
