import os


for file in os.listdir():
    if '.npy' in file:
        os.remove(file)
