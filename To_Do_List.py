import os, time
tasks = []
def add():
    task = input("\nEnter The Task : ")
    tasks.append(task)

def update():
    for i, task in enumerate(tasks):
        print(f'{(i+1)}. {task}')
    choice = int(input("\nEnter The Task Number You Want To Delete : "))
    del tasks[choice-1]
    print("\nTask Deleted Successfully\n")
    for i, task in enumerate(tasks):
        print(f'{(i+1)}. {task}')

def view():
        for i, task in enumerate(tasks):
            print(f'{(i+1)}. {task}')

print("----To The To Do List----\n")

while True:
    option = input("\nAdd Task\nUpdate Task\nView Tasks\nExit\n\nEnter Your Choice : ")
    option.lower()
    if option:
        os.system('cls' if os.name == 'nt' else 'clear')

    if option in ["add task","add"]:
        add()
    elif option in ["update task","update"]:
        update()
    elif option in ["view tasks","view"]:
        view()
    elif option in ["exit"]:
        break
    
