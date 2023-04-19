print("hello world")

import os

filenames = [f.name for f in os.scandir()]

print(filenames)