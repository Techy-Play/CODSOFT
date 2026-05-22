import secrets
import string


def build_charset(complexity):
	if complexity == 1:
		return string.ascii_letters
	if complexity == 2:
		return string.ascii_letters + string.digits
	return string.ascii_letters + string.digits + string.punctuation


def get_password_length():
	while True:
		try:
			length = int(input("Enter the desired password length: "))
			if length > 0:
				return length
			print("Please enter a positive whole number.")
		except ValueError:
			print("Please enter a valid whole number.")


def get_password_complexity():
	print("Choose password complexity:")
	print("1. Letters only")
	print("2. Letters and digits")
	print("3. Letters, digits, and symbols")

	while True:
		try:
			complexity = int(input("Enter your choice (1-3): "))
			if complexity in (1, 2, 3):
				return complexity
			print("Please choose 1, 2, or 3.")
		except ValueError:
			print("Please enter a valid number.")


def generate_password(length, complexity):
	charset = build_charset(complexity)
	return "".join(secrets.choice(charset) for _ in range(length))


def main():
	print("Password Generator")
	length = get_password_length()
	complexity = get_password_complexity()
	password = generate_password(length, complexity)
	print(f"Generated Password: {password}")


if __name__ == "__main__":
	main()
