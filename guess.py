# 產生 1~100 隨機整數讓使用者猜
# 猜對印出'猜對了!'
# 猜錯要告訴使用者比答案大/小

import random

start = input('請決定隨機數字起始值: ')
end = input('請決定隨機數字終止值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0

while True:
	num = input('1~100 請猜數字: ')
	num = int(num)
	count = count + 1
	if num == r:
		print('猜對了!')
		print('總共猜了', count, '次')
		break
	elif num > r:
		print('猜的數字比答案大')
	else:
		print('猜的數字比答案小')
	print('總共猜了', count, '次')