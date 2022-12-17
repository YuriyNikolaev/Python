# filename class_1.py

class Person:
	name = "Tom"

	def display_info(self):
		print("Привет, меня зовут", self.name)

person1 = Person()
person1.display_info() # Привет, меня зовут Tom

person2 = Person()
person2.name = "Sam"
person2.display_info() # Привет, меня зовут Sam