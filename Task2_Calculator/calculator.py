def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("Please enter a valid number.")


def get_operation():
	print("Choose an operation:")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	while True:
		choice = input("Enter your choice (1-4): ").strip()
		if choice in {"1", "2", "3", "4"}:
			return choice
		print("Please choose a valid option from 1 to 4.")


def calculate(first_number, second_number, operation):
	if operation == "1":
		return first_number + second_number
	if operation == "2":
		return first_number - second_number
	if operation == "3":
		return first_number * second_number
	if second_number == 0:
		return None
	return first_number / second_number


def main():
	print("Simple Calculator")
	first_number = get_number("Enter the first number: ")
	second_number = get_number("Enter the second number: ")
	operation = get_operation()

	result = calculate(first_number, second_number, operation)

	if result is None:
		print("Error: Division by zero is not allowed.")
	else:
		print(f"Result: {result}")


if __name__ == "__main__":
	main()
