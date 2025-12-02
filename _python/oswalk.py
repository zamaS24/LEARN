import os

curr_dir = os.getcwd()

# it goes through each folder and subfoler 
# yields the folder and its filenames and somthing _ 
# we care about the files that come in dirname 
# we print them by joining them so basicaly we walk each file that exists in tat curr_dir 
for dirname, _, filenames in os.walk(curr_dir):

    pass
    # for filename in filenames:
    #     print(os.path.join(dirname, filename))


