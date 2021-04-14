class item:
	# Step 1 - add constructor to initialize the members of this class.
	def __init__(self, name, price, quantity):
		#	constructor code is added here ...
		self._name = name
		self._price = price
		self._quantity = quantity

		
	# Step 2 - add getters to retrieve the value connected to the members of this class. 
	
	# Stringify the results to be displayed to the user 
	# based on the item properties.
	def __str__(self):
		return (str(self._name) + "\t" + str(self._price) + "\t" + str(self._quantity) + "\t" + str(round((self._price*self._quantity),2)))
 	



