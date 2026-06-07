## CodSoft Python Projects

This repository contains Python mini-projects completed for the CodSoft internship.

### Task 1: To-Do List Application

A simple command-line based To-Do List application built using Python.

#### Features
- Add new tasks
- View all tasks
- Delete tasks
- Persistent task storage using text files
- Input validation
- Terminal screen clearing for better user experience

#### How It Works
- Tasks are stored in a `task.txt` file
- Tasks remain saved even after closing the program
- Users can manage tasks using a menu-driven interface

#### How to Run

```bash
python Task1_TodoList/todo.py
```

### Task 2: Calculator

A simple command-line calculator that performs basic arithmetic operations on two user-provided numbers.

#### Features
- Prompts the user for two numbers
- Lets the user choose an arithmetic operation
- Supports addition, subtraction, multiplication, and division
- Handles invalid input and division by zero

#### How It Works
- The user enters two numbers
- The user selects an operation from the menu
- The program performs the calculation and displays the result

#### How to Run

```bash
python Task2_Calculator/calculator.py
```

### Task 3: Password Generator

A command-line password generator that creates strong, random passwords based on the length and complexity chosen by the user.

#### Features
- Prompts the user for the desired password length
- Lets the user choose password complexity
- Generates random passwords using secure random selection
- Prints the password directly on the screen

#### How It Works
- The user enters a password length
- The user selects a complexity level: letters only, letters and digits, or letters, digits, and symbols
- The program builds a matching character set and generates a random password

#### How to Run

```bash
python Task3_PasswordGenerator/gen.py
```