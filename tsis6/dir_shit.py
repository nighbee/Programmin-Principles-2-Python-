import os,  string
#1 listing directories and files in path
path=input('Enter your shitty path: ')
os.chdir(path)
print(os.listdir(path))
#2
if os.path.exists(path):
    filename=os.path.basename(path)
    directory=os.path.diname(path)
    print(filename, directory)
else:
    print('Not found')

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
#5 list to file
items=['mango', 'orange', 'apple', 'lemon']
with open(file_name) as f:
    for it in items:
        f.write(it+"\n")
    f.close()
# 6 generate 26 files which names A to Z.txt
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)
#7 copy and paste to another doc
second_file=input('Second file which u gonna paste info from first one: ')
with open(file_name, 'r') as f:
    with open(second_file, 'w') as f1:
        for line in f:
            f1.write(line)
        f1.close()
    f.close()

#8
if os.path.exists(path):
    f=input('enter file name which wanna to delete: ')
    os.chdir(path)
    os.remove(f)
else:
    print('Path not found! resubmit')


