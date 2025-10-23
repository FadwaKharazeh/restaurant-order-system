menu = { 
    "Pizza":10,
    "Burger":5,
    "Shawarma":7,
    "Fries":2,
    "Juice":3
}
for item in menu:
    print(f"{item} : {menu[item]} JD")
orders = []
num_items = int(input("Enter how many item you want to order:"))
for i in range(num_items):
   dish_name = input("Enter the name of the item:")
   quantity = int(input("Enter the quantity:"))
   orders.append((dish_name,  quantity))
Total = 0
for order in orders:
    dish_name=order[0]
    quantity=order[1]
    if dish_name in menu:
        subtotal=menu[dish_name]*quantity
        Total=Total+subtotal
        print(f"{dish_name} = {subtotal}JD")
    else:
        print(f"{dish_name} not found in the menu")
print(f"Total = {Total}JD")