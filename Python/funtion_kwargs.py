def order_pizza(name , address , **toppings):
    print(f"Name is {name}")
    print(f"Your order will be delivered to {address}")
    total_price=200
    for i in toppings.items():
        total_price = total_price+10
    print(f"Total price is {total_price}")
order_pizza("sagar" , "hatia", chessse = True , origano = True , chiliflex = True )
