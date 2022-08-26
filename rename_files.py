import os 

dirname = input('Enter the directory: ')
os.chdir(dirname)

dirlist = os.listdir()

#print(dirlist)

lead = input('What label do you want for the files?')

file_number = 1

# This is an example for rename pictures
for filename in dirlist:
    if filename.endswith('.jpg'):
        newname = lead  + str(file_number) + '.jpg'
        os.rename(filename, newname)
        file_number +=1