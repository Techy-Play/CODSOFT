tasks = [] #initialized list to store tasks
# TODO List for CODSOFT Project Internship Task

# Function to clear terminal screen
def clear_screen():
  import os
  os.system("cls || clear")


# Function to load tasks from text file
def loadFile():
  global tasks
  try:
    with open("task.txt", "r") as f:
       tasks = [x.strip() for x in f]
  except FileNotFoundError:
    open("task.txt", "w").close()
    print("Task.txt file now found. Creating new file...\nFile Created Sucessfully! You can now add tasks to your list!\n\n")

# Function to save updated tasks into file
def updateFile():
  with open("task.txt", "w") as f:
    for tsk in tasks:
      f.write(tsk +"\n")

# Function to add new task
def newTask():
  newTask = input("Enter new task: ")
  tasks.append(newTask)

# Function to display all tasks
def viewTask():
  if len(tasks) == 0:
    print("Task list is Empty, Try adding some tasks and try again!")
  else:
    for x in range(len(tasks)):
      print(f"{x+1}. {tasks[x]}")

# Function to delete selected task
def delTask():
  viewTask()
  if tasks:
    try:
      a = input("Enter the Task number to Delete: ")
      inp = int(a)
      if 1 <= inp <=len(tasks):
        tasks.pop(inp -1)
        print("Task Removed! This is new Task List: \n")
        viewTask()
      else:
        print("Enter valid list number.")
    except ValueError:
      print("Enter the Numeric Value !")
  else:
    print("Nothing to Delete on the Task list!")


# Main program loop
def main():
  clear_screen()
  loadFile()
  while True:
    print("""Select the operation you want to perform:\n
      \t1. Add new Task
      \t2. View all Tasks
      \t3. Remove Task from the List
      \t4. Exit""", end='\n')
    choice = input("Enter Your choice: ")
    if choice == '1':
      clear_screen()
      newTask()
      print("Task Added!")
      input("Press Enter to continue...")
      clear_screen()

    elif choice == '2':
      clear_screen()
      print("These are your current Tasks list: \n")
      viewTask()
      inp = input("Press Enter to go back to menu: \n\n")
      if inp == '':
        clear_screen()
        pass
    elif choice == '3':
      clear_screen()
      delTask()

      inp = input("Press Enter to save and go back to menu: \n\n")
      if inp == '':
        clear_screen()
        pass
    elif choice == '4':
      break
    else:
      print("Choose Valid operation!!!")
    updateFile()

# Finally called main function to run the whole program :)
main()