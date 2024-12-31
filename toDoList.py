from sys import exit
from shlex import split
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

toDo = {}

manual = """
HELP | H                                                                            WRITES DOWN THIS
ADD | A <TASKNAME> [--PRIORITY | -P PRIORITY] [--STATUS | -S STATUS]                ADDS ASKED ITEM
REMOVE | REM | R <TASKNAME>                                                         REMOVES ASKED ITEM
UPDATE | U <OLDNAME> <NEWNAME> [--PRIORITY | -P PRIORITY] [--STATUS | -S STATUS]    EDITS ASKED ITEM AND UPDATES THE VALUES
WRITE | SHOW | PRINT                                                                WRITES DOWN THE TO DO LIST
CLEAR | CLS                                                                         CLEARS TERMINAL
EXIT | QUIT                                                                         KILLS THE PROGRAM
"""

def add2List(taskName="UNTITLED", priority="NOT SET", status="NOT DONE"):
    validPriorities = ["LOW", "MEDIUM", "HIGH", "NOT SET"]
    if priority not in validPriorities:
        print(f"ERROR: INVALID PRIORITY... SETTING PRIORITY to 'NOT SET'.")
        priority = "NOT SET"
    toDo[taskName] = [priority, status]

def findListItem(taskName):
    return toDo.get(taskName, None)

def writeList():
    if toDo:
        for idx, (key, value) in enumerate(toDo.items(), start=1):
            print(f"{idx}. {key} -> PRIORITY: {value[0]}; STATUS: {value[1]}")
    else:
        print("TO DO IS EMPTY!")

def removeListItem(taskName):
    if taskName in toDo:
        del toDo[taskName]
        print(f"REMOVED!")
    else:
        print(f"ERROR: TASK NOT FOUND!")

def updateList(oldName, newName, newPriority="NOT SET", newStatus="NOT DONE"):
    if oldName in toDo:
        toDo[newName] = [newPriority, newStatus]
        if oldName != newName:
            del toDo[oldName]
        print(f"UPDATED!")
    else:
        print(f"ERROR: TASK NOT FOUND!")

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
    try:
        clear()
        while True:
            try:
                cmd = split(input("~\TODO\LIST1$ ").strip())
                if not cmd:
                    continue
                command = cmd[0].upper()
                if command in ("EXIT", "QUIT"):
                    exit("GOODBYE!")
                elif command in ("CLEAR", "CLS"):
                    clear()
                elif command in ("HELP", "H"):
                    print(manual)
                elif command in ("ADD", "A"):
                    cleanCmd, priority, status = parseFlags(cmd[1:])
                    if not cleanCmd:
                        print("ERROR: GOT NO NAME!")
                        continue
                    add2List(cleanCmd[0], priority, status)
                    print(f"ADDED!")
                elif command in ("REM", "REMOVE"):
                    if len(cmd) < 2:
                        print("ERROR: GOT NO NAME!")
                        continue
                    removeListItem(cmd[1])
                elif command in ("UPDATE", "U"):
                    cleanCmd, priority, status = parseFlags(cmd[1:])
                    if len(cleanCmd) < 2:
                        print("ERROR: NEED OLD AND NEW NAME!")
                        continue
                    updateList(cleanCmd[0], cleanCmd[1], priority, status)
                elif command in ("WRITE", "PRINT", "SHOW"):
                    writeList()
                else:
                    print("INVALID COMMAND!")
            except Exception as e:
                print(f"ERROR: {e.upper()}")
    except Exception as e:
        print(f"ERROR: {e.upper()}")
if __name__ == "__main__":
    main()
