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
        return self.location, self.year_built, self.price_purchased


def display_house_info(house):
    print("-----------------------")
    print("House Information:")
    print("Year Built:", house.year_built)
    print("Location:", house.location)
    print("Price Purchased: $" + str(round(house.price_purchased, 2)))
    print("Current Value: $" + str(round(house.current_value, 2)))


def main():
    while True:
        try:
            year_built = int(input("Year built: "))
            price = float(input("Purchase price: "))
            current_year = int(input("Current year: "))
            location = input("Location: ")

            if current_year < year_built:
                print("Error: Current year can't be before the house was built.")
                continue

            house = House(year_built, price, location)
            house.calculate_current_value(current_year)

            display_house_info(house)
            print("------------------------")
            print("Profit Earned: $" + str(round(house.money_earned(), 2)))
            print("------------------------")

        except ValueError:
            print("Invalid input. Please enter correct data types.")
            continue

        again = input(
            "Would you like to enter another house? (yes/no): ").lower()
        if again != 'yes':
            print("Farewell!")
            break


main()
