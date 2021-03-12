import os

target = r"E:\Development\python-projects\py-dir-word-counter\directoryToCheck"
os.chdir(target)
print(os.listdir())
f = open("test.txt")
print(f.read())

