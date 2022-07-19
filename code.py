# Entering the modules
import time
import os
import shutil

# Entering the path, which depends on the user
path = input("Enter your path: ")

# Creating the variable days, and converting the amount of days into seconds using time.time()
days = input("Enter number of days: ")
seconds = time.time() - (days * 24 * 60 * 60)

if os.path.exists(path):
    os.listdir()
    os.walk(path)

os.path.join(path, user)




