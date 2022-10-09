class cheesecakes():
	def __init__(self, fat_cottage_cheese, egg, salt, vegetable_oil, flour, time):
		self.fat_cottage_cheese = fat_cottage_cheese
		self.egg = egg
		self.salt = salt
		self.vegetable_oil = vegetable_oil
		self.flour = flour = 1,
		self.time = time
	def cooking(self):
		print('Я готовлю:', self.time, 'минут')
	def goodies(self):
		if self.time < 5:
			readiness = 'не готово'
		else:
			readiness = 'готово'
		print("Я поел")
blin = cheesecakes(fat_cottage_cheese = 5, egg = 3, salt = 10, vegetable_oil = 2,flour = 1, time = 6 )
blin.cooking()
blin.goodies()