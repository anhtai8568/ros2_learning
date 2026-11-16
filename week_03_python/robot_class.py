class Robot:
	def __init__(self, name, speed):
		self.name = name 
		self.speed = speed

	def move(self):
		print("Robot", self.name, "is moving at speed", self.speed)

	def stop(self):
		print("Robot", self.name, "stopped")


robot1 = Robot("Alpha", 20)
robot2 = Robot("Beta", 10)
robot1.move()
robot1.stop() 
robot2.move()
robot2.stop()
