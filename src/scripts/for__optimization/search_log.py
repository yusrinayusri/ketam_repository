#######
# Description : search log file by keyword and print lines
# Author : https://github.com/yusrinayusri
# Updates : 
#   20-Jan-2024 : Initial commit
######
import sys

# search function
def search_log_file(file_path, keyword):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

            matching_lines = [line.strip() for line in lines if keyword in line]

            if matching_lines:
                print(f"Lines containing '{keyword}':")
                for line in matching_lines:
                    print(line)
            else:
                print(f"No lines containing '{keyword}' found.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
# define arguments to parameters
log_file_path = sys.argv[1]
search_keyword = sys.argv[2]

search_log_file(log_file_path, search_keyword)

