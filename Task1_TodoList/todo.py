tasks = [] #initialized list to store tasks
# TODO List for CODSOFT Project Internship Task


def clear_screen(a):
  if a == True:
    import os
    os.system("cls||clear")
    print("\n" * 50)
  else:
    pass


def loadFile():
  global tasks
  try:
    with open("task.txt", "r") as f:
       tasks = [x.strip() for x in f]
  except:
    task = open("task.txt", "w")
    print("Task.txt file now found. Creating new file...")


def updateFile():
  with open("task.txt", "w") as f:
    for tsk in tasks:
      f.write(tsk +"\n")


def newTask():
  newTask = input("Enter new task: ")
  tasks.append(newTask)


def viewTask():
  if len(tasks) == 0:
    print("Task list is Empty, Try adding some tasks and try again!")
  else:
    for x in range(len(tasks)):
      print(x+1,". ", tasks[x])

  
def delTask():
  viewTask()
  if len(tasks) != 0:
    try:
      a = input("Enter the Task number to Delete: ")
      inp = int(a)
      tasks.pop(inp -1)
      print("Task Removed! This is new Task List: \n")
      viewTask()
    except:
      print("Enter the Numeric Value !")
  else:
    print("Nothing to Delete on the Task list!")



def main():
  loadFile()
  while True:
    print("""Select the operation you want to perform:\n
      \t1. Add new Task
      \t2. View all Tasks
      \t3. Remove Task from the List
      \t4. Exit""", end='\n')
    choice = input("Enter Your choice: ")
    if choice == '1':
      clear_screen(True)
      newTask()
      print("Task Added!")

    elif choice == '2':
      clear_screen(True)
      print("These are your current Tasks list: \n")
      viewTask()
      inp = input("Press Enter to go back to menu: ")
      if inp == '':
        pass
    elif choice == '3':
      clear_screen(True)
      delTask()

      inp = input("Press Enter to save and go back to menu: ")
      if inp == '':
        pass
    elif choice == '4':
      break
    else:
      print("Choose Valid operation!!!")
      clear_screen(False)
    updateFile()
main()