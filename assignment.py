def calculate_total_cost(sales,profit, ship_mode):
    surcharge = 0 
    if ship_mode == "Same Day":
        surcharge = 0.2
    elif ship_mode == "First Class":
        surcharge = 0.1
    elif ship_mode == "Standard Class":
        surcharge = 0.05

    total_cost = (sales-profit)*(1+surcharge)
    return total_cost 

# calculate_total_cost function with the sales, profit and ship_mode values to get the total cost.
# Example:

# python
sales = 100
profit = 20
ship_mode = "Same Day"
total_cost = calculate_total_cost(sales,profit,ship_mode)
print(total_cost)


