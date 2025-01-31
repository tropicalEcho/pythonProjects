from shlex import split
import os, sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Store multiple to-do lists
todo_lists = {}
selected_list = None

manual = """
HELP | H                          PRINTS THIS
LISTS                            SHOWS ALL TODO LISTS
SELECT <LISTNAME>                SELECTS A TODO LIST
CREATE <LISTNAME>                CREATES A NEW TODO LIST
DELETE <LISTNAME>                DELETES A TODO LIST
ADD | A <TASKNAME>                ADDS ASKED ITEM
    [-P | --PRIORITY PRIORITY]    SETS PRIORITY OF THE TASK
    [--STATUS | -S STATUS]        SETS STATUS OF THE TASK
REMOVE | REM | R <TASKNAME>       REMOVES ASKED ITEM
UPDATE | U <OLDNAME> <NEWNAME>    EDITS ASKED ITEM AND UPDATES THE VALUES
    [-P | --PRIORITY PRIORITY]    SETS PRIORITY OF THE TASK
    [--STATUS | -S STATUS]        SETS PRIORITY OF THE TASK
WRITE | SHOW | PRINT              WRITES DOWN THE TO DO LIST
CLEAR | CLS                       CLEARS TERMINAL SCREEN
EXIT | QUIT                       KILLS THE PROGRAM
"""

def add2List(taskName="UNTITLED", priority="NOT SET", status="NOT DONE"):
    if selected_list is None:
        print("ERROR: NO LIST SELECTED!")
        return
    validPriorities = ["LOW", "MEDIUM", "HIGH", "NOT SET"]
    if priority not in validPriorities:
        print(f"ERROR: INVALID PRIORITY... SETTING PRIORITY TO 'NOT SET'.")
        priority = "NOT SET"
    todo_lists[selected_list][taskName] = [priority, status]
    print("ADDED!")

def writeList():
    if selected_list is None:
        print("ERROR: NO LIST SELECTED!")
        return
    if todo_lists[selected_list]:
        for idx, (key, value) in enumerate(todo_lists[selected_list].items(), start=1):
            print(f"{idx}. {key} -> PRIORITY: {value[0]}; STATUS: {value[1]}")
    else:
        print("TO DO IS EMPTY!")

def removeListItem(taskName):
    if selected_list is None:
        print("ERROR: NO LIST SELECTED!")
        return
    if taskName in todo_lists[selected_list]:
        del todo_lists[selected_list][taskName]
        print("REMOVED!")
    else:
        print("ERROR: TASK NOT FOUND!")

def updateList(oldName, newName, newPriority="NOT SET", newStatus="NOT DONE"):
    if selected_list is None:
        print("ERROR: NO LIST SELECTED!")
        return
    if oldName in todo_lists[selected_list]:
        todo_lists[selected_list][newName] = [newPriority, newStatus]
        if oldName != newName:
            del todo_lists[selected_list][oldName]
        print("UPDATED!")
    else:
        print("ERROR: TASK NOT FOUND!")

def parseFlags(cmd):
    priority = "NOT SET"
    status = "NOT DONE"
    cleanCmd = []
    
    i = 0
    while i < len(cmd):
        if cmd[i] in ("--PRIORITY", "-P") and i + 1 < len(cmd):
            priority = cmd[i + 1].upper()
            i += 2
        elif cmd[i] in ("--STATUS", "-S") and i + 1 < len(cmd):
            status = cmd[i + 1].upper()
            i += 2
        else:
            cleanCmd.append(cmd[i])
            i += 1
            
    return cleanCmd, priority, status

def main():
    global selected_list
    try:
        clear()
        while True:
            try:
                cmd = split(input(f"~\\toDo\\{selected_list if selected_list else 'NO LIST SELECTED'}$ ").strip())
                if not cmd:
                    continue
                command = cmd[0].upper()
                
                if command in {"EXIT", "QUIT"}:
                    sys.exit("GOODBYE!")
                elif command in {"CLEAR", "CLS"}:
                    clear()
                elif command == "HELP":
                    print(manual)
                elif command == "LISTS":
                    print("AVAILABLE TODO LISTS:", ", ".join(todo_lists.keys()) if todo_lists else "NONE")
                elif command == "CREATE":
                    if len(cmd) < 2:
                        print("ERROR: NO LIST NAME GIVEN!")
                        continue
                    list_name = cmd[1]
                    if list_name in todo_lists:
                        print("ERROR: LIST ALREADY EXISTS!")
                    else:
                        todo_lists[list_name] = {}
                        print(f"CREATED TODO LIST: {list_name}")
                elif command == "SELECT":
                    if len(cmd) < 2:
                        print("ERROR: NO LIST NAME GIVEN!")
                        continue
                    list_name = cmd[1]
                    if list_name in todo_lists:
                        selected_list = list_name
                        print(f"SELECTED TODO LIST: {selected_list}")
                    else:
                        print("ERROR: LIST NOT FOUND!")
                elif command == "DELETE":
                    if len(cmd) < 2:
                        print("ERROR: NO LIST NAME GIVEN!")
                        continue
                    list_name = cmd[1]
                    if list_name in todo_lists:
                        del todo_lists[list_name]
                        if selected_list == list_name:
                            selected_list = None
                        print(f"DELETED TODO LIST: {list_name}")
                    else:
                        print("ERROR: LIST NOT FOUND!")
                elif command == "ADD":
                    cleanCmd, priority, status = parseFlags(cmd[1:])
                    if not cleanCmd:
                        print("ERROR: GOT NO NAME!")
                        continue
                    add2List(cleanCmd[0], priority, status)
                elif command in {"REM", "REMOVE"}:
                    if len(cmd) < 2:
                        print("ERROR: GOT NO NAME!")
                        continue
                    removeListItem(cmd[1])
                elif command == "UPDATE":
                    cleanCmd, priority, status = parseFlags(cmd[1:])
                    if len(cleanCmd) < 2:
                        print("ERROR: NEED OLD AND NEW NAME!")
                        continue
                    updateList(cleanCmd[0], cleanCmd[1], priority, status)
                elif command in {"WRITE", "PRINT", "SHOW"}:
                    writeList()
                else:
                    print("INVALID COMMAND!")
            except Exception as e:
                print(f"ERROR: {str(e).upper()}")
    except Exception as e:
        print(f"ERROR: {str(e).upper()}")

if __name__ == "__main__":
    main()