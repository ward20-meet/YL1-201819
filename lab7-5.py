class Person():
   def __init__(self, name, favorite_food, age ):
       self.name = name
       self.fav_food = favorite_food
       self.age = age


   def color(self, color="Red"):
       self.color = color

   def print_info(self):
       print("My name is " + self.name + ", I'm " + str(self.age) + " years old.")
       print("My favorite food is " + self.fav_food + " and my favorite color is " + self.color)


a = Person("Britney", "Pizza", 16)
a.color("Black")
a.print_info()

b = Person("Jake", "children" , 15)
b.print_info()

