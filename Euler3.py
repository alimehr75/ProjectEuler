def finde(n):
	i = 2
	while n != 1:
		if n % i == 0:
			n /= i
			prime_big = i
		else:
			i += 1
	return prime_big


num = int(input("your number : "))
if __name__ == "__main__":
	print(finde(num))
