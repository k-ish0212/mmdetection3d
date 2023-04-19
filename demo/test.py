print("hello world")

import os

filenames = [f.name for f in os.scandir("../")]


print(filenames)

filenames = [f.name for f in os.scandir("../../")]

print(filenames)

filenames = [f.name for f in os.scandir("../../var/")]

print(filenames)

filenames = [f.name for f in os.scandir("../../var/data/")]

print(filenames)