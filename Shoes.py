class Shoes:
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)
    
    def check_budget(self, budget):
        if not isinstance(budget, (int, float)):
            print("Invalid entry")
            exit()
    
    def change(self, budget):
        return budget - self.price

    def buy(self, budget):
        self.check_budget(budget)

        if budget >= self.price:
            change_left = self.change(budget)
            print("You can cop some " + self.name + " with $" + str(round(change_left, 2)) + " left")
            if budget == self.price:
                print("You have exactly enough money")
        else:
            print("No, you cannot buy the shoes")

        print("Thank you for using our shoes app")
