def fibonachi(a, b):
	a_list = []
	while a < 4e+6:
		a_list.append(a)
		a, b = a + b, a
	even_sum = 0
	for even_num in a_list:
		if even_num % 2 == 0:
			even_sum += even_num
	return even_sum


print(fibonachi(0, 1))
