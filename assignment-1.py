import os
import shelve
import shutil

studentinfo1={'name':'Xubingjie','sex':'Female','Country':'China','City':'Hangzhou'}
# Create /open file
with shelve.open('test02.bin') as fp: # Create or open a binary file
    fp['1']=studentinfo1  # Write data to a file in dictionary form
    # Readfile (returns file content)
    print(fp['1'])

#Get the current directory with getcwd first 
shutil.copy("test02.bin.dat","test02.bin")
shutil.move("test02.bin.dat","movetest02.bin")
# Delete file
os.remove('test02.bin')



