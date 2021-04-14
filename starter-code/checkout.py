from shoppingcart import shoppingcart
class checkout:
	obj = shoppingcart()
	print("Welcome to the online shopping portal")
	print("------------------------------------------------")
	while(True):
		print("Tell us what did you shop?")
		name = input("Enter item name:")
		price = float(input("Enter item price:"))
		quantity = int(input("Enter item quantity:"))
		obj.addItemToCart(name, price, quantity)
		print("------------------------------------------------")
		print("Total price so far:" + str(obj.getTotalPrice()))
		print("------------------------------------------------")
		repeat = input("Do you want to checkout? (y/n)")
		if (repeat == "n"):
			continue;
		else:
			obj.displayItemsDuringCheckout()
			print("Please pay:" + str(obj.getTotalPrice()))
			print("------------------------------------------------")
			break