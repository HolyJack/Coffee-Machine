# Define coffee machine
class CoffeeMacnhine:
    class Coffee:
        def __init__(self, name, water, milk, beans, cost):
            self.name = name
            self.water = water
            self.milk = milk
            self.beans = beans
            self.cost = cost

    # Types of coffee
    COFFEE = [Coffee('espresso', 250, 0, 16, 4),
              Coffee('latte', 350, 75, 20, 7),
              Coffee('cappucino', 200, 100, 12, 6)]

    # Actions
    BUY = 'buy'
    FILL = 'fill'
    TAKE = 'take'
    REMAINING = 'remaining'
    EXIT = 'exit'

    def __init__(self, money, water, milk, beans, disposable_cups):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans
        self.in_menu = False
        self.disposable_cups = disposable_cups

    def action(self, string):
        if self.in_menu:
            self.action_menu(string)
        elif string == self.BUY:
            if not self.in_menu:
                self.in_menu = True
                return "menu"
        elif string == self.FILL:
            self.fill()
        elif string == self.TAKE:
            self.take()
        elif string == self.REMAINING:
            self.logs()
        return string

    def action_menu(self, choice):
        if choice != 'back':
            choice = COFFEE[int(choice) - 1]
            self.buy(choice.water, choice.milk, choice.beans, choice.cost)
        self.in_menu = False

    def buy(self, water, milk, beans, cost):
        if self.water < water:
            print("Sorry, not enough water!")
        elif self.milk < milk:
            print("Sorry, not enough milk!")
        elif self.beans < beans:
            print("Sorry, not enough beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough cups!")
        else:
            self.water -= water
            self.milk -= milk
            self.beans -= beans
            self.money += cost
            self.disposable_cups -= 1
            print("I have enough resources, making you a coffee!")

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add:")
        self.beans += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.disposable_cups += int(input())

    def take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0

    def logs(self):
        print("""The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
{} of money""".format(self.water,
                      self.milk,
                      self.beans,
                      self.disposable_cups,
                      self.money))
        print()


# Define coffee
class Coffee:
    def __init__(self, name, water, milk, beans, cost):
        self.name = name
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


# Types of coffee
COFFEE = [Coffee('espresso', 250, 0, 16, 4),
          Coffee('latte', 350, 75, 20, 7),
          Coffee('cappucino', 200, 100, 12, 6)]

# New coffee machine
coffee_machine = CoffeeMacnhine(550, 400, 540, 120, 9)

MENU = 'menu'
EXIT = 'exit'

status = ''
while status != EXIT:
    if status == MENU:
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    else:
        print("Write action (buy, fill, take, remaining, exit):")
    status = coffee_machine.action(input())
