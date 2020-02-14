def gdc(x, y):
	while y != 0:
		x, y = y, x % y
	return x


number = 1
last_range = int(input("number = "))
for i in range(1, last_range + 1):
	number = int((number * i) / gdc(number, i))
print(number)
