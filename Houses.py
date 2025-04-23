class House:
    def __init__(self, year_built, price_purchased, location):
        self.year_built = year_built
        self.price_purchased = price_purchased
        self.location = location
        self.current_value = 0.0

    def calculate_current_value(self, current_year):
        rate = 0.08
        age = current_year - self.year_built
        self.current_value = self.price_purchased * ((1 + rate) ** age)

    def money_earned(self):
        return self.current_value - self.price_purchased

    def __str__(self):
        result = "House Info:"
        result += " Year Built: " + str(self.year_built)
        result += " Location: " + self.location
        result += " Price Purchased: $" + str(round(self.price_purchased, 2))
        result += " Current Value: $" + str(round(self.current_value, 2))
        return result


def main():
    year_built = int(input("Year built: "))
    price = float(input("Purchase price: "))
    current_year = int(input("Current year: "))
    location = input("Location: ")

    if current_year < year_built:
        print("Error: Current year can't be before the house was built.")
        return

    house = House(year_built, price, location)
    house.calculate_current_value(current_year)

    print(house)
    print("Profit Earned: $" + str(round(house.money_earned(), 2)))


main()
