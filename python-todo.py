todo = []
completed = []

def add_task(task):
    todo.append(task)

def remove_task(task):
    todo.remove(task)

def completed_task(task):
    completed.append(task)
    todo.remove(task)

def view_todo():
   print("This is your todo list")
   print(todo)

def view_completed():
    print("These are the task which are completed")
    print(completed)

while True:
    choices = int(input("1.add task\n2.remove task\n3.mark complete\n4.view todo\n5.view completed\n6.Exit\n"))
    if(choices == 1):
        task = input("Enter task to add in todo: ")
        add_task(task)
    elif(choices == 2):
        task = input("Enter task to remove in todo: ")
        remove_task(task)
    elif(choices == 3):
        task = input("Enter task to add as completed: ")
        completed_task(task)
    elif(choices == 4):
        view_todo()
    elif(choices == 5):
        view_completed()
    elif(choices == 6):
        exit(0)
    else:
        print("Enter a valid choice")