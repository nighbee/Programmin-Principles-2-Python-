import os
# print(os.getcwd())
def createFile(fname):
    if os.path.exists(fname+'.txt'):
        print('File exists!')
    else:
        with open(fname+'.txt', 'w') as f:
            print('File created!')
            f.close()
def readFile(fname):
    if os.path.exists(fname+'.txt'):
        with open(fname+'.txt', 'r') as f:
            content=f.read()
            print('Here it goes:', content)
            f.close()
    else:
        print('Such file doesnt exist!')

def appendFile(fname):
    if os.path.exists(fname+'.txt'):
        with open(fname+'.txt', 'a') as f:
            new_add=input('new text to add:')
            f.write(new_add)
            f.close()
            print('text added!')
    else:
        print('create File first!')


def overwriteFile(fname):
    if os.path.exists(fname+'.txt'):
        with open(fname+'.txt', 'w') as f:
            new_content=input('Input content:')
            f.write(new_content)
            print('File overwritten!')
            f.close()
    else:
        print('Not found!')


def removeFile(fname):
    if os.path.exists(fname+'.txt'):
        os.remove(fname+'.txt')
        print("file deleted")
    else:
        print('file doesnt exist!')


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input(
    'Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)
else:
    print('Something went wrong!')
