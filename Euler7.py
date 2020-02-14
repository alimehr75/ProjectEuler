def is_prime(n):
	it_prime = True
	for k in range(2, int(n ** 0.5) + 1):
		if n % k == 0:
			it_prime = False
			break
	return it_prime


i, j = 0, 2
while i < 10001:
	if is_prime(j):
		i += 1
	j += 1
print(j - 1)
