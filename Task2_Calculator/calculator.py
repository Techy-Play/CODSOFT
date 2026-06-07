def get_number(prompt):
	"""Prompt the user for a number and validate the input.

	Repeatedly asks the user for input until a valid float can be
	returned. This centralizes input validation so the main flow stays
	simple and focused on calculation logic.

	Args:
		prompt (str): The text shown to the user when asking for input.

	Returns:
		float: The parsed numeric value entered by the user.
	"""
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			# Inform the user and repeat the prompt on invalid input
			print("Please enter a valid number.")


def get_operation():
	"""Display available operations and get a validated selection.

	Presents a simple numbered menu and ensures the user selects one
	of the supported operations (1-4). Returning the choice as a
	string keeps compatibility with the existing `calculate` function.

	Returns:
		str: One of '1', '2', '3', or '4' representing the operation.
	"""
	print("Choose an operation:")
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")

	while True:
		choice = input("Enter your choice (1-4): ").strip()
		if choice in {"1", "2", "3", "4"}:
			return choice
		# Keep prompting until a valid selection is made
		print("Please choose a valid option from 1 to 4.")


def calculate(first_number, second_number, operation):
	"""Perform the selected arithmetic operation.

	The function accepts two numeric operands and a string code for the
	operation. For division, it returns `None` when dividing by zero so
	callers can handle that case explicitly.

	Args:
		first_number (float): The left-hand operand.
		second_number (float): The right-hand operand.
		operation (str): '1' for add, '2' for subtract, '3' for multiply,
					'4' for divide.

	Returns:
		float|None: The calculation result, or `None` for division by zero.
	"""
	if operation == "1":
		return first_number + second_number
	if operation == "2":
		return first_number - second_number
	if operation == "3":
		return first_number * second_number

	# Only remaining supported operation is division ('4'):
	if second_number == 0:
		# Signal an error condition (division by zero) via None
		return None
	return first_number / second_number


def main():
	# High-level program flow: greet the user, collect inputs, compute,
	# and show the result or an appropriate error message.
	print("Simple Calculator")
	first_number = get_number("Enter the first number: ")
	second_number = get_number("Enter the second number: ")
	operation = get_operation()

	result = calculate(first_number, second_number, operation)

	if result is None:
		# Only possible when user chose division and attempted to divide
		# by zero.
		print("Error: Division by zero is not allowed.")
	else:
		print(f"Result: {result}")


if __name__ == "__main__":
	main()
