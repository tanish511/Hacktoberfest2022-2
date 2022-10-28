# A optimized school method based Python program to check
# if a number is composite.

def isComposite(n):

	# Corner cases
	if (n <= 1):
		return False
	if (n <= 3):
		return False

	# This is checked so that we can skip
	# middle five numbers in below loop
	if (n % 2 == 0 or n % 3 == 0):
		return True
	i = 5
	while(i * i <= n):
		
		if (n % i == 0 or n % (i + 2) == 0):
			return True
		i = i + 6
		
	return False

# Driver Program to test above function

print("true") if(isComposite(11)) else print("false")
print("true") if(isComposite(15)) else print("false")
# This code is contributed by Anant Agarwal.
