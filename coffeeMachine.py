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
   |            (__  \
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
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    return (0.01*pennies + 0.1*dimes + 0.05*nickles + 0.25*quarters)

def resource_check(coffee):
    if (resources["coffee"] >= MENU[coffee["coffee"]] and resources["water"] >= MENU[coffee["water"]] and 
        resources["milk"] >= MENU[coffee["milk"]] if coffee != "espresso" else True):
        resources["coffee"] -= MENU[coffee["coffee"]]
        resources["water"] -= MENU[coffee["water"]]
        resources["milk"] -= MENU[coffee["milk"]] if coffee != "espresso" else True
        return True
    else:
        print("Sorry there is not enough resources.")
    return False

choice = input("What would you like? (espresso/latte/cappuccino): ")
while True:
    if choice == "espresso":
        value = money()
        if value >= MENU["espresso"["cost"]] and resource_check(choice):
            value -= MENU["espresso"["cost"]]
            print(f"Here is ${value} in change")
            enjoy()
    elif choice == "latte":
        value = money()
        if value >= MENU["latte"["cost"]] and resource_check(choice):
            value -= MENU["latte"["cost"]]
            print(f"Here is ${value} in change")
    elif choice == "cappuccino":
        value = money()
        if value >= MENU["cappuccino"["cost"]] and resource_check(choice):
            value -= MENU["cappuccino"["cost"]]
            print(f"Here is ${value} in change")
            resource_check(choice)
            enjoy()
    elif choice == "report":
        print(resources)
    else:
        print("Invalid Input")




