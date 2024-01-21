#######
# Description : Sort files in the directory based on file types
# Author : https://github.com/yusrinayusri
# Version : 1.0.0
# Updates : 
#  7-Jan-2024   : Initial commit
#  10-Jan-2024  : Follow pep-8 style guide for file naming
######
import os
import sys
import shutil

#passing argument into the path variable
path1 = sys.argv[1]

#list of required folders
folders = ['PDFs','EPUB','Docs','Excels','Others','Zipped Docs']

#function to create folders
def createFolders():
    try:
        for folder in folders:
            #check required folders exist or not
            if os.path.exists(folder):
                print(f"{folder} already exists. Moving on..")
            else:
                os.makedirs(folder)
                print(f"{folder} created successfully")
        print("Done creating all required folders.")
    except:
        print("Encountered issues. please retry!")

#function to move files to respective folders
def movePDFFiles():
    #pdf files
    pdf_folder = [file for file in os.listdir() if file.lower().endswith('.pdf')]
    if pdf_folder:
        for pdf_file in pdf_folder:
            pdf_move_to_folder = 'PDFs/' + pdf_file
            shutil.move(pdf_file,pdf_move_to_folder)
            print(f"Moved {pdf_file}.")
        print("Moved all PDFs\n")
    else:
        print("No PDF files here.\n")

def moveDocsFiles():
    #docs files
    docs_folder = [file for file in os.listdir() if file.lower().endswith('.doc')]
    if docs_folder:
        for docs_file in docs_folder:
            docs_move_to_folder = 'Docs/' + docs_file
            shutil.move(docs_file,docs_move_to_folder)
            print(f"Moved {docs_file}.")
        print("Moved all Docs\n")
    else:
        print("No docs files here.\n")

def moveExcelsFiles():
    #excels files
    excel_folder = [file for file in os.listdir() if file.lower().endswith('.xls')]
    if excel_folder:
        for excel_file in excel_folder:
            excel_move_to_folder = 'Excels/' + excel_file
            shutil.move(excel_file,excel_move_to_folder)
            print(f"Moved {excel_file}.")
        print("Moved all Excels\n")
    else:
        print("No Excel files here.\n")

def moveEPUBFiles():
    #epub files
    epub_folder = [file for file in os.listdir() if file.lower().endswith('.epub')]
    if epub_folder:
        for epub_file in epub_folder:
            epub_move_to_folder = 'EPUB/' + epub_file
            shutil.move(epub_file,epub_move_to_folder)
            print(f"Moved {epub_file}.")
        print("Moved all EPUBs\n")
    else:
        print("No epub files here.\n")

def moveZipFiles():
    #zipped files
    zip_folder = [file for file in os.listdir() if file.lower().endswith('.zip')]
    if zip_folder:
        for zip_file in zip_folder:
            zip_move_to_folder = 'Zipped Docs/' + zip_file
            shutil.move(zip_file,zip_move_to_folder)
            print(f"Moved {zip_file}.")
        print("Moved all Zipped Files\n")
    else:
        print("No zipped files here.\n")

def moveOthersFiles():
    #others
    others_ext = ['.pdf','.doc','.docx','.xl','.epub','.zip','.gz']
    #get only files from the path
    others_only_file = [file for file in os.listdir() if os.path.isfile(os.path.join(path1,file))]
    print(f"Others file : \n {others_only_file}")
    if others_only_file:
        for others_file in others_only_file:
            others_move_to_folder = 'Others/' + others_file
            shutil.move(others_file,others_move_to_folder)
            print(f"Moved {others_file}.")
        print("Moved all Others")
    else:
        print("No others file here.\n")

#####################
###### MAIN () ######
#####################
        
#ensure we are at the correct path
if (os.getcwd()) != path1:
    print(f"You are at : {os.getcwd()}")
    print("Moving to correct path")
    os.chdir(path1)
    print(f"You are at : {os.getcwd()}\n")
else:
    print(f"You are at : {os.getcwd()}\n")

#consensus to start
agreeToContinue = input(print("Do you wish to sort files in this folder? press Y/N\n"))

if agreeToContinue == 'Y':
    try:
        print("Listing active files in the directory\n")
        print(os.listdir())
        print("\nCreating required folders => ")
        createFolders()
        print("\nMoving files into folders => ")
        movePDFFiles()
        moveDocsFiles()
        moveExcelsFiles()
        moveEPUBFiles()
        moveZipFiles()
        moveOthersFiles()
        print("\nScript finished executing.")
    except:
        print("There are 0 files to sort. Exiting.")
elif agreeToContinue == 'N':
    print("Exiting.")
else:
    print("Invalid input. Please re-run script")


    