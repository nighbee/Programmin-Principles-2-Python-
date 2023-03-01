import os
#1 listing directories and files in path
path=input('Enter your shitty path: ')
os.chdir(path)
print(os.listdir(path))
#2


# 3 check if path exists or not
print(os.path.exists(path))
#4 count nums of lines in file
file_name=input('Enter name of file with pdf/txt/docx shit like that: ')
with open(file_name, 'r') as f:
    count =0
    for lines in f:
        count+=1
    print(count)
    f.close()
# 5
