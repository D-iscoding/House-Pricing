def calculate_current_value(year_built, price_purchased, current_year):
    rate = 0.08
    age = current_year - year_built
    return price_purchased * ((1 + rate) * age)

def money_earned(current_value, price_purchased):
    return current_value - price_purchased

def display_house_info(year_built, location, price_purchased, current_value):
    print("-------------------")
    print("House Information:")
    print("Year Built:", year_built)
    print("Location:", location)
    print("Price Purchased: $" + str(round(price_purchased, 2)))
    print("Current Value: $" + str(round(current_value, 2)))

def main():
    while True:
        year_built = int(input("Year built: "))
        price_purchased = float(input("Price Purchased: "))
        current_year = int(input("Current year: "))
        location = input("Location: ")

        if current_year < year_built:
            print("Invalid input, Current year can't be before the house was built.")
        else:
            current_value = calculate_current_value(year_built, price_purchased, current_year)
            display_house_info(year_built, location, price_purchased, current_value)
            profit = money_earned(current_value, price_purchased)
            print("Profit Earned: $" + str(round(profit, 2)))
            print("-------------------")

        again = input("Would you like to enter another house? (yes/no): ").strip().lower()
        if again != 'yes':
            print("FareWell!")
            break

main()