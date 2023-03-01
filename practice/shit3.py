import os
path=input('Enter ur direct:')
os.chdir(path)
files=os.listdir(path)

larg = 0
largest_file = " "
for file in files:
    if os.path.isfile(file):
        size = os.path.getsize(file)
        if size >larg:
            larg=size
            largest_file=file
print("largest file in your path is:" + largest_file+" " +str(larg)+' bytes.')