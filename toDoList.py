import os, shlex

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def flashlight():
    manual = [
        'add <task> -p <priority> -c <category> -d <deadline>   : adds a task with optional priority, category, and deadline',
        'rem <task>                                             : removes a task',
        'edit <task> -p <priority> -c <category> -d <deadline>  : edits an existing task',
        'done <task>                                            : marks a task as done',
        'undone <task>                                          : marks a task as pending',
        'view or show                                           : list all existing tasks',
        'help                                                   : prints this',
        'exit                                                   : exits todo',
        'clear                                                  : clears the screen'
    ]
    for entry in manual: print(entry)

tasks = []

def add_task():
    task = " ".join(cmd[1:cmd.index('-p')]) if '-p' in cmd else " ".join(cmd[1:])
    priority = cmd[cmd.index('-p')+1] if '-p' in cmd else 'medium'
    category = cmd[cmd.index('-c')+1] if '-c' in cmd else 'general'
    deadline = cmd[cmd.index('-d')+1] if '-d' in cmd else None
    tasks.append({"label": task, "priority": priority, "category": category, "deadline": deadline, "isDone": False})
    print(f"'{task}' added with priority '{priority}', category '{category}', and deadline '{deadline}'.")


def edit_task():
    task_label = " ".join(cmd[1:cmd.index('-p')]) if '-p' in cmd else " ".join(cmd[1:])
    for task in tasks:
        if task["label"] == task_label:
            if '-p' in cmd: task["priority"] = cmd[cmd.index('-p')+1]
            if '-c' in cmd: task["category"] = cmd[cmd.index('-c')+1]
            if '-d' in cmd: task["deadline"] = cmd[cmd.index('-d')+1]
            print(f"'{task_label}' edited successfully!")
            return
    print(f"'{task_label}' not found!")

def not_found(task_found): 
    if not task_found:
        for items in cmd[1:]: print(f"'{items}' isn't on the list.")

def rem_task():
    task_label = " ".join(cmd[1:])
    for task in tasks:
        if task["label"] == task_label:
            tasks.remove(task), print(f"Task '{task_label}' removed!")
            return
    not_found(False)


def view():
    if not tasks: print("Your To Do is empty!")
    else:
        for idx, task in enumerate(tasks, 1):
            state = "DONE!" if task["isDone"] else "PENDING!"
            deadline_info = f", Deadline: {task['deadline']}" if task['deadline'] else ""
            print(f"Task {idx}: '{task['label']}', Priority: {task['priority']}, Category: {task['category']}, Status: {state}{deadline_info}")


def state(command):
    task_label = " ".join(cmd[1:])
    for task in tasks:
        if task["label"] == task_label:
            if command == "done": task["isDone"] = True
            else: task["isDone"] = False
            print(f"Task '{task_label}' marked as {'DONE' if command == 'done' else 'PENDING'}!")
            return
    not_found(False)


clear()
while True:
    cmd = shlex.split(input("./Tasks> "))
    command = cmd[0].lower()
    
    if command == "add": add_task()
    elif command == "rem": rem_task()
    elif command == "edit": edit_task()
    elif command in ["view", "show"]: view()
    elif command == "done": state("done")
    elif command == "undone": state("undone")
    elif command == "help": flashlight()
    elif command == "exit": exit()
    elif command == "clear": clear()
    else: print("Invalid command! 'help' to know about available commands.")
