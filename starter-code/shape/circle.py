import math
from round import round
class circle(round):
	def __init__(self,radius):
		super(circle, self).__init__()
		self.radius = radius
	def area(self):
		self.area = self.pi * pow(self.radius,2)
	def perimeter(self):
		self.perimeter = 2 * self.pi * self.radius