import math 
class RobotState: 
	def __init__(self,x,y,theta):
		self.x = x 
		self.y = y 
		self.theta = theta
		self.distance = 0
	def show(self):
		print(self.x, self.y, self.theta, self.distance)
	def move(self, dx, dy):
		self.x = self.x + dx
		self.y = self.y + dy
		self.distance +=  math.sqrt(dx**2 + dy**2)
	def rotate(self, dtheta):
		self.theta = self.theta + dtheta
robot1 = RobotState(0, 0 , 0) 

robot1.move(3,4)
robot1.move(0,2)
robot1.rotate(90)
robot1.show()
