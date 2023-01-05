import os
import warnings


def get_results():
    file = open("results.sarif", 'r')
    for i in file:
        print(i.lstrip())
        if i.lstrip().startswith('"id":'):
            exit("ERROR: There are security issues, please check security section!")
