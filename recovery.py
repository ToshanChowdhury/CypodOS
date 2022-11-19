import os
import time

print("Launching Recovery...")
time.sleep(10)

app_time = open("backup/app_time.py").read()
calendar = open("backup/calendar.py").read()
assistant = open("backup/assistant.py").read()
calculator = open("backup/Calculator.py").read()
codeeditor = open("backup/codeeditor.py").read()
color = open("backup/color.py").read()
file_manager = open("backup/file-manager.py").read()
loginsystem = open("backup/loginsystem.py").read()
main = open("backup/main.py").read()
notes = open("backup/notes.py").read()
settings = open("backup/settings.py").read()
setupos = open("backup/setupos.py").read()
store = open("backup/store.py").read()
terminal = open("backup/terminal.py").read()
webbrowser = open("backup/webbrowser.py").read()

print("backup/app_time.py --restore")
time.sleep(1)
print("backup/calendar.py --restore")
time.sleep(1)
print("backup/assistant.py --restore")
time.sleep(1)
print("backup/calculator.py --restore")
time.sleep(1)
print("backup/codeeditor.py --restore")
time.sleep(1)
print("backup/color.py --restore")
time.sleep(1)
print("backup/file_manager.py --restore")
time.sleep(1)
print("backup/loginsystem.py --restore")
time.sleep(1)
print("backup/main.py --restore")
time.sleep(1)
print("backup/notes.py --restore")
time.sleep(1)
print("backup/settings.py --restore")
time.sleep(1)
print("backup/setupos.py --restore")
time.sleep(1)
print("backup/store.py --restore")
time.sleep(1)
print("backup/terminal.py --restore")
time.sleep(1)
print("backup/webbrowser.py --restore")
time.sleep(1)

with open("app_time.py", "w") as f:
    f.write(app_time)

with open("calendar.py", "w") as f:
    f.write(calendar)

with open("assistant.py", "w") as f:
    f.write(assistant)

with open("Calculator.py", "w") as f:
    f.write(calculator)

with open("codeeditor.py", "w") as f:
    f.write(codeeditor)

with open("color.py", "w") as f:
    f.write(color)

with open("file-manager.py", "w") as f:
    f.write(file_manager)

with open("loginsystem.py", "w") as f:
    f.write(loginsystem)

with open("main.py", "w") as f:
    f.write(main)

with open("notes.py", "w") as f:
    f.write(notes)

with open("settings.py", "w") as f:
    f.write(settings)

with open("setupos.py", "w") as f:
    f.write(setupos)

with open("store.py", "w") as f:
    f.write(store)

with open("terminal.py", "w") as f:
    f.write(terminal)

with open("webbrowser.py", "w") as f:
    f.write(webbrowser)

os.mkdir("account_login_details")
os.mkdir("customize")

with open("customize/color_toolbar.txt", "w") as f:
    f.write("none")

with open("customize/menu_bar_color.txt", "w") as f:
    f.write("none")

print("Restored CypodOS, please setup your operating system")
input()
os.startfile("setupos.py")