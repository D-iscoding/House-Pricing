class House:
    def __init__(self, year_built=0, price_purchased=0.0, location="none", current_value=0.0):
        self.year_built = year_built
        self.price_purchased = price_purchased
        self.location = location
        self.current_value = current_value

    def calculate_current_value(self, current_year):
        rate = 0.08
        age = current_year - self.year_built
        self.current_value = self.price_purchased * ((1 + rate) ** age)

    def money_earned(self):
        return self.current_value - self.price_purchased

    def __str__(self):
        return f"\nHouse Info:\nYear Built: {self.year_built}\nLocation: {self.location}\nPrice Purchased: ${self.price_purchased:.2f}\nCurrent Value: ${self.current_value:.2f}"


def main():
    print("House Info Program")

    # Get user input
    year_built = int(input("Enter the year the house was built: "))
    price = float(input("Enter the price the house was purchased for: "))
    current_year = int(input("Enter the current year: "))
    location = input("Enter the location of the house: ")

    # Validate input
    if current_year < year_built:
        print("Error: Current year can't be before the house was built.")
        return

    # Create house object
    my_house = House(year_built, price, location)

    # Calculate value and print results
    my_house.calculate_current_value(current_year)

    print(my_house)
    print(f"Profit Earned: ${my_house.money_earned():.2f}")


main()
