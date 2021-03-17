# add your logic here ....
from circle import circle 


mycircle = circle(3.14)
mycircle.area()
mycircle.perimeter()
print(f"TESTING CIRCLE SHAPE\n---------------------------------")
print(f"Circle area = {str(round(mycircle.area, 2))}\nCircle perimeter = {str(round(mycircle.perimeter, 2))}")

