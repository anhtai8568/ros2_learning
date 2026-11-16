class RobotState: 
	def __init__(self,x,y,theta):
		self.x = x 
		self.y = y 
		self.theta = theta
	def show(self):
		print(self.x, self.y, self.theta)
	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy

class OmniRobot(RobotState):
	def omni_move(self):
		print("Omni robot can move in all direction")
omni1 = OmniRobot(4, 5, 10)
omni1.show()
omni1.move(40,21)
omni1.omni_move()
omni1.show()
