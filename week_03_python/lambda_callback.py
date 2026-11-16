callback = lambda step : print("Robot moving at step:", step)

def robot_loop(callback):
	for step in range (5):
		callback(step)

robot_loop(callback)
