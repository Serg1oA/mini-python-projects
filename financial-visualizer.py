print('''--------------------------------
----- FINANCIAL VISUALIZER -----
--------------------------------''')

# values below are annual, unless stated otherwise
salary = input("Annual Salary:\n")
if not salary.isnumeric():
    salary = input("Enter numbers only! Annual Salary:\n")

monthly_housing = input("Monthly Housing:\n")
if not monthly_housing.isnumeric():
    monthly_housing = input("Enter numbers only! Monthly Housing:\n")

monthly_bills = input("Monthly Bills:\n")
if not monthly_bills.isnumeric():
    monthly_bills = input("Enter numbers only! Monthly Bills:\n")

weekly_food = input("Weekly Food:\n")
if not weekly_food.isnumeric():
    weekly_food = input("Enter numbers only! Weekly Food:\n")

travel = input("Annual Travel:\n")
if not travel.isnumeric():
    travel = input("Enter numbers only! Annual Travel:\n")


# convert all input to annual values we're going to use
salary = float(salary)
housing = float(monthly_housing) * 12
bills = float(monthly_bills) * 12
food = float(weekly_food) * 52
travel = float(travel)

housing_percent = housing / salary * 100
bills_percent = bills / salary * 100
food_percent = food / salary * 100
traver_percent = travel / salary * 100
expenses = housing + bills + food + travel
extra = salary - expenses
extra_percent = extra / salary * 100

# tax based on salary
if salary < 10001:
    tax = 5 / 100 * salary
elif salary < 40001:
    tax = 10 / 100 * salary
elif salary < 80001:
    tax = 15 / 100 * salary
else:
    tax = 20 / 100 * salary
tax_percent = tax / salary * 100

print(f'''------------------------------------------------------------------------------
housing | $ {housing:10,.2f} | {housing_percent:5,.1f}% | {"#" * int(housing_percent)}
  bills | $ {bills:10,.2f} | {bills_percent:5,.1f}% | {"#" * int(bills_percent)}
   food | $ {food:10,.2f} | {food_percent:5,.1f}% | {"#" * int(food_percent)}
 travel | $ {travel:10,.2f} | {traver_percent:5,.1f}% | {"#" * int(traver_percent)}
    tax | $ {tax:10,.2f} | {tax_percent:5,.1f}% | {"#" * int(tax_percent)}
  extra | $ {extra:10,.2f} | {extra_percent:5,.1f}% | {"#" * int(extra_percent)}
-----------------------------------------------------------------------------''')