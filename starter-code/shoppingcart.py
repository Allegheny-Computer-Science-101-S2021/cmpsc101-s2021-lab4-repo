import ctypes
from item import item
class shoppingcart:
    # Step 1 - create a constructor
    def __init__(self):
        #total number of items in the cart
        self._itemCount = 0
        # total price of items in the cart
        self._totalPrice = 0.0
        # current cart capacity
        self._capacity = 5 
        # an array of items to be stored in the cart
        self._cart = self._create_array(self._capacity) # create an array using low-level array
    # call this method to create an array with space = capacity 
    def _create_array(self, c): # create array space
        # Return new array with capacity c
        return (c * ctypes.py_object)()  # see ctypes documentation
    # Step 2 - add an item to the Shopping Cart 
    def addItemToCart(self, name, price, quantity):
        pass
    # Step 3 - add the required logic to increase the size of the structure. 
    def increaseCartSize(): # similar to resize in darray.py
        pass        
    def getTotalPrice(self):
        return self._totalPrice
    def displayItemsDuringCheckout(self):
        print("------------------------------------------------")
        for i in range(self._itemCount):
            print(self._cart[i])
            print("------------------------------------------------");
        
    
