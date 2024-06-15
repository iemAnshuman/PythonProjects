print("""
      /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
""")
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

def enjoy():
    print("""
         {
      {   }
       }_{ __{
    .-{   }   }-.
   (   }     {   )
   |`-.._____..-'|
   |             ;--.
   |            (__  \\
   |             | )  )
   |             |/  /
   |             /  /    Enjoy!
   |            (  /
   \             y'
    `-.._____..-'
""")

def money():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    return (0.01*pennies + 0.1*dimes + 0.05*nickels + 0.25*quarters)

def resource_check(coffee):
    ingredients = MENU[coffee]["ingredients"]
    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    for item in ingredients:
        resources[item] -= ingredients[item]
    return True

while True:
    choice = input("What would you like? (espresso/latte/cappuccino/report/exit): ").lower()
    if choice == "exit":
        break
    if choice in MENU:
        value = money()
        if value >= MENU[choice]["cost"] and resource_check(choice):
            change = value - MENU[choice]["cost"]
            print(f"Here is ${change:.2f} in change")
            enjoy()
        else:
            print("Sorry, that's not enough money. Money refunded.")
    elif choice == "report":
        print(resources)
    else:
        print("Invalid Input")
