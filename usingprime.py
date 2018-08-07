from primecode import is_prime

def main():
	num = int(input("Enter the number: "))
	if is_prime(num):
		print(num, "is a Prime Number")
	else:
		print(num, "is not a Prime number")
main()
