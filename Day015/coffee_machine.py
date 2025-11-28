should_make_another_coffee = True
LATTE_COST = 2.5
ESPRESSO_COST = 1.5
CAPPUCCINO_COST = 2.0

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0
}

required_resources = [
    {
        'espresso': {'water': 50, 'coffee': 18, 'milk': 0},
        'latte': {'water': 200, 'coffee': 24, 'milk': 150},
        'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100},
    }
]

def check_if_sufficient(coffee):
    is_enough_coffee = False
    is_enough_milk = False
    is_enough_water = False
    if resources['water'] >= required_resources[0][coffee]['water']:
        is_enough_water = True
    if resources['milk'] >= required_resources[0][coffee]['milk']:
        is_enough_milk = True
    if resources['coffee'] >= required_resources[0][coffee]['coffee']:
        is_enough_coffee = True
    if not is_enough_water:
        print(f'Sorry there is not enough water.')
    if not is_enough_milk:
        print(f'Sorry there is not enough milk.')
    if not is_enough_coffee:
        print(f'Sorry there is not enough coffee.')
    return is_enough_coffee, is_enough_milk, is_enough_water

def calculate_money():
    quarters = int(input('How many quarters?:'))
    dimes = int(input('How many dimes?:'))
    nickels = int(input('How many nickles?:'))
    pennies = int(input('How many pennies?:'))
    return 0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies

def check_if_money_are_enough(drink, money):
    if drink == 'espresso' and money >= ESPRESSO_COST:
         return True
    elif drink == 'latte' and money >= LATTE_COST:
        return True
    elif drink == 'cappuccino' and money >= CAPPUCCINO_COST:
        return True
    else:
        return False

def calculate_change(money, drink):
    if drink == 'espresso':
        return money - ESPRESSO_COST
    elif drink == 'latte':
        return money - LATTE_COST
    else:
        return money - CAPPUCCINO_COST

def deduct_resources(coffee_type):
    if coffee_type == 'espresso':
        resources['water'] -= 50
        resources['coffee'] -= 18
    elif coffee_type == 'latte':
        resources['water'] -= 200
        resources['coffee'] -= 24
        resources['milk'] -= 150
    else:
        resources['water'] -= 250
        resources['coffee'] -= 24
        resources['milk'] -= 100

while should_make_another_coffee:
    print('What would you like? (espresso/latte/cappuccino):')
    coffee_type = input().lower()
    if coffee_type == 'report':
        print(f'Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\n'
              f'Coffee: {resources["coffee"]}g\nMoney: ${resources["money"]}')
    elif coffee_type.lower() == 'off':
        should_make_another_coffee = False
    else:
        is_sufficient = check_if_sufficient(coffee_type)
        if is_sufficient:
            print('Please, insert coins:')
            money = calculate_money()
            is_enough_money = check_if_money_are_enough(coffee_type, money)
            if not is_enough_money:
                print('Sorry that\'s not enough. Money refunded.')
            else:
                change = calculate_change(money, coffee_type)
                resources['money'] =resources['money']+ (money-change)
                if change > 0:
                    print(f'Here is ${change:.2f} dollars in change.')
                deduct_resources(coffee_type)
                print(f'Here is your {coffee_type}. Enjoy!☕️”')