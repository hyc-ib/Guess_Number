# 產生 1~100 隨機整數讓使用者猜
# 猜對印出'猜對了!'
# 猜錯要告訴使用者比答案大/小

import random
r = random.randint(1, 100)

while True:
	num = input('1~100 請猜數字: ')
	num = int(num)
	if num == r:
		print('猜對了!')
		break
	elif num > r:
		print('猜的數字比答案大')
	else:
		print('猜的數字比答案小')