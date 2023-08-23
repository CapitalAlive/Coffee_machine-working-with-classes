git init && git symbolic-ref HEAD refs/heads/main
class CoffeeMachine:
    def __init__(self):
        # water, milk, beans, cups, cash
        self.espresso_info = [250, 0, 16, 1, 4]
        self.latte_info = [350, 75, 20, 1, 7]
        self.cappuccino_info = [200, 100, 12, 1, 6]
        self.machine_info = [400, 540, 120, 9, 550]
        self.action_status = None
        self.machine_status = None
        self.input = ""

    def __str__(self):
        return (f"""
    The coffee machine has:
    {self.machine_info[0]} ml of water
    {self.machine_info[1]} ml of milk
    {self.machine_info[2]} g of coffee beans
    {self.machine_info[3]} disposable cups
    ${self.machine_info[4]} of money
    """)

    def reset_variables(self):
        self.machine_status = None
        self.action_status = None
        self.input = None
        self.menu(None)

    def menu(self, user_input):
        self.input = user_input

        if self.machine_status is None:
            print("Write action (buy, fill, take, remaining, exit):\n")
            self.machine_status = "getting_choice"
        elif self.machine_status == "buying":
            self.buy()
        elif self.machine_status == "filling":
            self.fill()
        elif self.input == "buy":
            self.machine_status = "buying"
            self.buy()
        elif self.input == "fill":
            self.machine_status = "filling"
            self.action_status = "msg_1"
            self.fill()
        elif self.input == "remaining":
            print(self)
            self.reset_variables()
        elif self.input == "take":
            print(f"\nI gave you ${self.machine_info[4]}\n")
            self.machine_info[4] = 0
            self.reset_variables()
        else:
            exit()

    def buy(self):
        if self.action_status is None:
            print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: \n")
            self.action_status = "choosing"
        elif self.input == "back":
            self.reset_variables()
        else:
            options = {"1": self.espresso_info, "2": self.latte_info, "3": self.cappuccino_info}
            choice = options[self.input]
            for n in range(4):
                if self.machine_info[n] - choice[n] < 0:
                    missing_element = ["water", "milk", "beans", "cups"][n]
                    print(f"Sorry, not enough {missing_element}!")
                    self.reset_variables()
                    return
            print("I have enough resources, making you a coffee!\n")
            print(self.machine_status, self.action_status)
            self.machine_info = [self.machine_info[n] - choice[n] for n in range(4)] + (
                [self.machine_info[4] + choice[4]])
            self.reset_variables()

    def fill(self):
        if self.action_status == "msg_1":
            print("\nWrite how many ml of water you want to add:\n")
            self.action_status = "water"
        elif self.action_status == "water":
            self.machine_info[0] += int(self.input)
            print("Write how many ml of milk you want to add:\n")
            self.action_status = "milk"
        elif self.action_status == "milk":
            self.machine_info[1] += int(self.input)
            print("Write how many grams of coffee beans you want to add:\n")
            self.action_status = "beans"
        elif self.action_status == "beans":
            self.machine_info[2] += int(self.input)
            print("Write how many disposable cups you want to add:\n")
            self.action_status = "cups"
        elif self.action_status == "cups":
            self.machine_info[3] += int(self.input)
            self.reset_variables()


    def start(self):
        user_input = None
        while True:
            self.menu(user_input)
            user_input = input()


my_machine = CoffeeMachine().start()
