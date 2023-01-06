import os
import warnings
from datetime import date

for i in os.listdir():
    if i.endswith('.sarif'):
        file = open(i, 'r')
        break
# direc = "Security Reports"
# try:
#     os.mkdir(direc)
#     cur_direc = os.path.join(direc, date.today())
#     os.mkdir(cur_direc)
    
# expect:
    
for i in file:
#     if i.lstrip().startswith('"id":'):
    print(i)
warnings.warn("Warning: There are security issues, please check security section!")
