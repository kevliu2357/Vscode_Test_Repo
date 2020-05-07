import math
import sys
from os import rename

import numpy
import requests

# print(sys.version)
print(sys.executable)  # commenting

# print a


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


r = requests.get("https://coreyms.com")
print(r.status_code)


# name = input("Your Name? ")
# print("Hello,", name)   ## use " run in the terminal"


# import numpy as np
# print(np.exp(1))

# import tushare as ts
# print(ts.get_hist_data('600848'))

# cmd+shift+p  command pallet

# ctrl + ~  show terminal

# cmd + k   clear terminal

# in terminal : pwd

# option+shift+f : auto formatting

# ctrl + space : editor ... save on

# command pallet :  sort imports

# ctrl + option + N
