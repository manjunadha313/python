# file operations : different operations that we can perform it on files..


# opening the file
# we have 2 syntax for opening a file
# 1) open()
# 2) with open()

#  mode :  its nothing but how i have to open the file
    # read - r
    # write - w
    # append - a

# `1st  syntax
# with open('fileoperations/dialog.txt','r') as file_object:
#     read_data = file_object.read()
#     print(read_data)
#     for ele in read_data:
#         print(ele)

#     readline_data = file_object.readline()
#     print(readline_data)
#     print(file_object.readline)

#     readlines_data = file_object.readlines()
#     print(readlines_data[1])
     
# writing:

# write()
# writelines()

with open('fileoperations/dialog.txt','w') as file_object:
    # write_data = file_object.write("i am a job seeker")
    # print(write_data)
     writelines_data = file_object.writelines(['hello my name is manjunadha\n',
        'i am from allagadda\n',
        'i am currently in hyderabad '])
     print(writelines_data)

