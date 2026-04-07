#Write a python script to print the current date in the following format  “Sun Sept 29 02:26:23 IST 2025”. 

import time

ltime = time.localtime();
print("%a %b %d %H:%M:%S %Z %Y",ltime )