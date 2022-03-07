#!/usr/bin/python

import os
import shutil

# Get current working directory

current_dir = os.getcwd()
print("Current directory: ", current_dir)

# Change current working directory

os.chdir("/Users/mat/Documents/myWorks/testpress/python/directory")

current_dir = os.getcwd()
print("Current directory: ", current_dir)

# List files and folders under a directory

list_of_files = os.listdir()
print("List of files in {}: {}".format(current_dir, list_of_files))

# Create a directory

os.mkdir("/Users/mat/Documents/myWorks/testpress/python/directory/test")

# Rename a directory

os.rename("test", "test-new")

# Delete a directory (If the directory is empty)

os.rmdir("test-new")

# In order to remove a non-empty directory, we can use the rmtree() method inside the shutil module.

shutil.rmtree('test')