import os
import time

def loop():
	os.system("color 02")
	os.system("cls")
	time.sleep(1)
	for a in range(1,11,1):
		for i in range(a):
			print("#",end="")
		for i in range(10,a,-1):
			print("-",end="")
		print("["+str(a*10)+"%]")

		if(a<10):
			time.sleep(1)
			os.system("cls")
		else:
			print("[<3]Download completed!")

loop()