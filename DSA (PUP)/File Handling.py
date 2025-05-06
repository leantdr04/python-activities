"""File Handling in Python- by Dela Rosa, Leant Nathaniel I."""
#1.
def StringCounter(filedir, word):                   #Function for string counter in a text file
    content = filedir.read()                        #Reads text file
    string_count = content.count(word)              #Counts how many times the string appeared inside txt file
    print(f"\nThe amount of times the string \'based\' used: {string_count}")    #Display number of occurrences

print("\n--String Counter--")
filetxt = open("File handling test.txt", 'r')       #Input file name that is in current working directory
word = "based"                                     #Word/string to count
StringCounter(filetxt, word)                      #Initiates the function
filetxt.close()                                   #Closes text file

#2.
import os       #imports os module

def FileSearch(folderdir, filename):                            #function for searching file from a directory
    if os.path.exists(folderdir):                               #Check if directory exists
        for root, dirs, files in os.walk(folderdir):            #Checks each directory and files
            if filename in files:
                print(f"\'{filename}\' is found in {folderdir}")    #Displays that file is in directory
    else:
        print("Path folder does not exist")

print("\n--File Search--")
path = input("Enter your folder directory: ")
_file = input("Enter file name to find: ")
print("Note: Program will exit if file is not found\n")

FileSearch(path, _file)         #Initiates function
