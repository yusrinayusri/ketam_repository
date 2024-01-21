#######
# Description : Delete (1) file in the directory
# Author : https://github.com/yusrinayusri
# Updates : 
#   7-Jan-2024  : Initial commit
#   10-Jan-2024 : Follow pep-8 style guide for file naming
######
import os
import sys

#pass argument into a variable
file_to_delete = sys.argv[1]

#print current directory
print(f"You are at : {os.getcwd()}")
#get consensus to delete file
agreeToContinue = input(print(f"Do you wish to remove {file_to_delete}? press Y/N\n"))
#deleting file
if agreeToContinue == 'Y':
    if os.path.exists(file_to_delete):
        try:
            os.remove(file_to_delete)
            print(f"{file_to_delete} removed.\n")
            print(os.getcwd())
        except:
            print("No access to delete. Please check script permission.\n")
            print("Make sure the script access is -rwxr-xr-x")
    else:
        print("File does not exist.")
elif agreeToContinue == 'N':
    print("No files deleted.")
else:
    print("Invalid input. Please re-run script")
    