import sys
import os
import time

def printLog(msg):
    print("[INFO] {} || {}".format(time.time(), msg))

def startJupyterNotebook(name, targetPath):
    jupyterNotebookName = name + ".ipynb"
    if jupyterNotebookName not in os.listdir(targetPath):
        os.system("cp Untitled.ipynb {}".format(jupyterNotebookName))
        os.system("mv {} {}".format(jupyterNotebookName, targetPath))
    os.chdir(targetPath)
    os.system("jupyter notebook {} &".format(jupyterNotebookName))

def main():

    try:
        target = sys.argv[1].lower()
        name = sys.argv[2].lower()
    except IndexError:
        printLog("1. python sup.py note <name>")
        printLog("2. python sup.py project <name>")
        return

    if target == "note":
        notesDirectory = "notes"
        jupyterTargetPath = notesDirectory
        
        if not os.path.isdir(notesDirectory):
            os.mkdir(notesDirectory)
        
    elif target == "project":
        projectsRootDirectory = "myprojects"
        projectDirectory = os.path.join(projectsRootDirectory, name)
        jupyterTargetPath = os.path.join(projectDirectory, "src")

        if not os.path.isdir(projectsRootDirectory):
            os.mkdir(projectsRootDirectory)

        if not os.path.isdir(projectDirectory):
            os.mkdir(projectDirectory)
            os.mkdir(jupyterTargetPath)
    else:
        printLog("1. python sup.py note <name>")
        printLog("2. python sup.py project <name>")
        return

    startJupyterNotebook(name, jupyterTargetPath)
    

if __name__ == "__main__":
    main()
