# import needed libraries
# used for interfacing with os (file scanning and removal)
import os
# not necessary, just used for timing code execution
from timeit import default_timer as timer

# sets working directory path, change to whatever is needed
path = r"C:\Users\admin\Desktop\Tumblr Files\Literally Just 3.7k Pictures of Catra"

# changes working directory to path
os.chdir(path)

# gets current working directory
cwd = os.getcwd()
# makes sure current working directory is the same as the given path
if cwd == path:
    print("Yer in the right place lad")

# program execution start time
start = timer()

# initialzes an empty set to hold future hashes of images
fileHashes = set()
# iterates through files in given directory and removes any duplicates
for file in os.listdir():
    # creates a location variable that holds the path to the current file
    loc = path+"\\"+file
    print("Checking", loc)
    # reads file (uses "with" to close immediately after reading; frees memory)
    with open(loc, "rb") as filebytes:
        # creates a hash of the file for easy comparison between file
        filehash = hash(filebytes.read())
    # if the file's hash is already in the hash list, removes duplicate file
    if filehash not in fileHashes:
        fileHashes.add(filehash)
    else:
        os.remove(loc)
        print("Deleting", file)

# program execution end time
end = timer()

print("Cleanse complete in", (end - start), "seconds")
