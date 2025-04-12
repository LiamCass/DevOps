# Python 3.10+
# Temporary program
# used to generate all 'hello world' files with proper extensions
# works in conjunction with "programming-languages.json"
# As this is a temporary program, ensure that both are in the same dir

import json
import os

JSON_PATH = "src/programming-languages.json"

def get_all_extensions(): pass
def get_all_languages():  pass
def create_files(
        path: str|os.PathLike=os.path.dirname(os.path.abspath(__file__)),
        name: str="hello",
        extensions: set={".txt"}):
    """
    Creates multiple files with the same names, but one for each different extension listed. Pretty weird outside of this temporary setup program.
    @param path: Defines the folder where the new files will be created. Defaults to location of this python file
    @param name: Defines the name of all files to be created, minus the file extension
    @param extensions: List of strings, each being the extensions to be tagged onto the filename. This function will create a new file for each one listed.
    """
    # For each extension, create a path and 'touch' the file.
    for i in extensions:
        filename = name+i
        filepath = os.path.join(path, filename)
        open(filepath, 'a').close()

if __name__ == "__main__":
    create_files()