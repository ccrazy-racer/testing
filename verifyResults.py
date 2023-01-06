import os
import warnings
from datetime import date

file = open("results.html", 'r')
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
