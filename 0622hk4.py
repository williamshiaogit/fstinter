import time
import os
import colorama

colorama.init(True)

a=0
while a == 0:
	for i in range(0,10,1):
		os.system("cls")
		i+=1
		if i-1 >= 0 and i-1 <= 4:
			print(colorama.Back.RED+colorama.Fore.RED+"abc")
			print(i)
			# time.sleep()
		elif i-1 >= 5 and i-1 <= 5:
			print("  ",colorama.Back.YELLOW+colorama.Fore.YELLOW+"abc")
			print(i)
		else:
			print("     ",colorama.Back.GREEN+colorama.Fore.GREEN+"abc")
			print(i)
		time.sleep(1)