with open('newFile.txt', 'w') as file:
    file.writelines(['Hello  World \n', 'This is a new line \n', 'This is another line \n'])
   
   
# adding exceptions to the file handling
try:
    with open('sample/newFile.txt', 'w') as file:
        file.writelines(['Hello  World \n', 'This is a new line \n', 'This is another line \n'])
except Exception as e:
    print("Error found: ",e)