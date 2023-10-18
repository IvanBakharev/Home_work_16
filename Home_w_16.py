                        # Задание первое

class Cassa:
	def __init__(self):
		self.count = 0;
	
	def top_up(self, x):
		self.count += x
		print(self.count)
	
	def count_1000(self):
		return int(self.count / 1000)

	def take_away(self, x):
		if x > self.count:
			raise Exception("Недостаточно денег в кассе")
		self.count -= x
		print(self.count)

cassa = Cassa()

try:
	cassa.top_up(3000)
	cassa.top_up(500)
	print(cassa.count_1000())
	cassa.take_away(1000)
	cassa.take_away(5000)
except Exception as err:
	print(err)
	
                      # Задание второе

class Turtle:
    def __init__(self, x, y, s):
        self.x, self.y, self.s = x, y, s  # Инициализация позиции и размера шага черепахи
    
    def go_up(self, step=1):
        self.y += self.s * step  

    def go_down(self, step=1):
        self.y -= self.s * step  

    def go_left(self, step=1):
        self.x -= self.s * step  

    def go_right(self, step=1):
        self.x += self.s * step  

    def evolve(self):
        self.s += 1  # Увеличение размера шага на 1
    
    def degrade(self):
        if self.s <= 1:
            raise Exception("Черепаха не может быть размером меньше 1")  
        self.s -= 1  
    
    def count_moves(self, x2, y2):
        dx, dy = abs(x2 - self.x), abs(y2 - self.y)  # Вычисление абсолютных разностей координат

        if dx % self.s != 0 or dy % self.s != 0:
            return None  # Возвращаем None, если указанные координаты недостижимы с текущим размером шага
        if (dx // self.s + dy // self.s) % 2 != 0:
            return None  # Возвращаем None, если количество шагов по x и y должно быть одинаковым (четное число шагов)
        return int(dx + dy) // self.s  # Возвращаем количество шагов для достижения указанных координат
    
turtle = Turtle(0, 0, 1)  
try:
    turtle.evolve()  
    print(turtle.count_moves(5, 5))  # Вывод минимального количества шагов для достижения координат (5, 5)
    turtle.degrade()  
    turtle.degrade()  
except Exception as err:
    print(err)                       