"""This program is to traverse in a string"""

import os
path = "."

files = os.listdir(path)
for name in files:
  print(name)
