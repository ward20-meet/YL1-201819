class Rectangle(object)
	def __init__(self,width,height):
		self.width = width
		self.height = height

	def Area(self):
		return self.width * self.height
	def Parameter(self):
		return (self.width + self.height) * 2 :
	def Print_properties(self):
		print(self.width + self.height)