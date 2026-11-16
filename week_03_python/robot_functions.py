speed = [12,10,9,11]

def work(speed):
	tong = 0 
	for sp in speed:
		tong += sp
	return tong/len(speed)

avg = work(speed)
print(avg)
