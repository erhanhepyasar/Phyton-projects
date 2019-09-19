from datetime import datetime
import time

while True:
	with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".txt", "w") as myfile:
		myfile.write("Hi there!")
	time.sleep(5)