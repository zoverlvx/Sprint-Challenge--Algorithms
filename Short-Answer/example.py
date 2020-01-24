sum = 0
n = 10

for i in range(n):
	j = 1
	print("here is i: ", i)
	while j < n:
		j *= 2
		sum += 1
		print(sum)
