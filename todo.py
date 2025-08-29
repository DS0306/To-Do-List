import json,os,uuid
from datetime import datetime
FILE="tasks.json"
VALID_STATUSES={"todo","done","in-progress"}

#STORAGE
def now():
    return datetime.now().isoformat(timespec="seconds")

def load_tasks():
    if os.path.exists(FILE):
        with open(FILE,'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(FILE,'w') as f:
        json.dump(tasks,f,indent=2)

tasks=load_tasks()

#OPERATIONS
def add_tasks():
    description=input("Add task description ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    t={
        "id":uuid.uuid4().hex[:8],
        "description":description,
        "status":"todo",
        "createdat":now(),
        "updatedat":now()

}
    tasks.append(t)
    save_tasks(tasks)
    print(f"Task added: [{t['id']}] {t['description']}")

def view_tasks():
    if not tasks:
        print("No tasks available. Please add a task.")
        return 
    else:
        print("\n#   ID  | Status   | Created  | Updated    | Description  ")
        print("-"*85)
        for i, task in enumerate(tasks, 1):
            print(f"{i:<2} {task['id']:<7} | {task['status']:<9} | {task['createdat']:<12} | {task['updatedat']:<12} | {task['description']}")

def pick_taskby_index(prompt="Enter task number : "):
    if not tasks:
        print("No tasks available.")
        return None
    view_tasks()
    raw=input(f"{prompt}").strip()
    try:
        index=int(raw)
        if 1 <=index <= len(tasks):
            return index-1
        print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None


def delete_tasks():
        if not tasks:
            print("No tasks to delete")
            return 
        index=pick_taskby_index("Enter task number to delete : ")
        if index is None:
            return
        remove=tasks.pop(index)
        save_tasks(tasks)   
        print(f"Task deleted: [{remove['id']}] {remove['description']}")    

def show_menu():
    print("\n To-Do List")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice=input("Enter your choice:")
    if choice=="1":
        add_tasks()
    elif choice=="2":
        view_tasks()
    elif choice=="3":
        delete_tasks()
    elif choice=="4":
        print("Exiting the program")
        break
    else:
        print("Invalid choice, please try again")
        

show_menu()

