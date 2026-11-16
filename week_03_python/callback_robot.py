def call_back(step):
	print("Callback at step", step)

def robot_loop(call_back):
	for step in range (3):
		call_back(step) 
robot_loop(call_back)  
   
