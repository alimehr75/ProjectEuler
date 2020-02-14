a_list = []
for i in range(900, 1000):
	for j in range(900, 1000):
		number = i * j
		if str(number) == str(number)[::-1]:
			a_list.append([number, i, j])
print(max(a_list))
