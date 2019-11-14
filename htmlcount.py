import os
from banner import banner

banner("HTML Tags Counter", 'william vollmer')

def get_full_path(name):
    filename = os.path.join(".", "testing", f"{name}")
    return filename

def load(name):
    data = []
    filename = get_full_path(name)
    print(f"...... loading from {filename}")
    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())
    return data

def tag_in(line):
    tag = "<"
    count = 0
    previouse_char = None
    for char in line:
        if char != "/" and previouse_char == "<":
            count = count +1
        previouse_char = char
    return count

def main():
    filename = input("please enter the name of html file: ")
    lines = load(filename)
    count = 0
    for line in lines:
        count = count + tag_in(line)
    print(f"the file {filename} contains {count} tags")

def run_event_loop():
    while True:
        main()
        command = input("would you like to count another html file (Y/N) ")
        if command.upper() == "Y":
            pass
        elif command.upper() == "C":
            print("{name}")
            break
        elif command.upper() == "G":
            print("✋ ☟✌✞☜ 👌☜☜☠ ☹⚐⚐😐✋☠☝ ☞⚐☼ ✡⚐🕆 ✌💧 🕈☜☹☹.")
        else:
            break
    return True

run_event_loop()