

stock_prices = [("AAPL", 190), ("MSFT", 350), ("TSLA", 180), ("ICE", 200)]

for i in stock_prices:
    print(i)

print("-------------------")

for ticker, price in stock_prices:
    print(price)

print("-------------------")

work_hours = [("Abby", 100), ("Billy", 400), ("Cassie",800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for  name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = name
        else:
            pass

    return(employee_of_month, current_max)

print(employee_check(work_hours))