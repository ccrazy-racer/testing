import os
from datetime import date
from zipfile import ZipFile
import shutil

for i in os.listdir():
    if i.endswith('.sarif'):
        filename = i
        file = open(i, 'r')
        break

direc = "Security_Reports"
date = str(date.today())

path_direc = os.path.join(direc)
cur_direc = os.path.join(direc, date)

if os.path.exists(path_direc):

    # This checks for pervious day unzipped folders, if any then zips that folder.
    list_dirs = os.listdir(path_direc)
    if len(list_dirs) != 0:
        for j in list_dirs:
            if len(j) != 0 and j.endswith('.zip') == False:
                if j.split('.')[0] != date:
                    name = j
                    zip_name = shutil.make_archive(
                        name, 'zip', os.path.join(direc, name))
                    try:
                        shutil.move(zip_name, os.path.join(
                            direc))
                    except PermissionError:
                        print("Permission denied.")

                    try:
                        shutil.rmtree(os.path.join(direc, name))
                    except OSError as error:
                        print(error)

    if os.path.exists(cur_direc):
        try:
            shutil.copyfile(filename, os.path.join(direc, date, filename))
        except PermissionError:
            print("Permission denied.")
    else:
        os.mkdir(cur_direc)
        try:
            shutil.copyfile(filename, os.path.join(direc, date, filename))
        except PermissionError:
            print("Permission denied.")
else:
    os.mkdir(direc)
    os.mkdir(cur_direc)
    try:
        shutil.copyfile(filename, os.path.join(direc, date, filename))
    except PermissionError:
        print("Permission denied.")

for i in file:
    if i.lstrip().startswith('"id":'):
        print(i)
