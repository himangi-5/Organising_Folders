import os
import shutil

# asking user to enter a folder that he/she wants to organise
location = input("Enter the directory that you want to sort :- ")

#storing all the files/folders in a variable
list_Of_Files = os.listdir(location)
# print(list_Of_Files)

#iterating on each and every file
for file in list_Of_Files:
    #spliting root name and extensions
    name, ext = os.path.splitext(file)

    #resolving the issue of folder(that have no extension)
    if ext ==" ":
        continue

    if os.path.exists(location+"/"+ext):
        shutil.move(location+"/"+file, location+"/"+ext+"/"+file)
    else:
        os.mkdir(location+"/"+ext)
        shutil.move(location+"/"+file, location+"/"+ext+"/"+file)
