import sys
import os
import time

def printLog(msg):
    print("[INFO] {} || {}".format(time.time(), msg))

def startJupyterNotebook(name, targetPath):
    jupyterNotebookName = name + ".ipynb"
    os.system("cp Untitled.ipynb {}".format(jupyterNotebookName))
    os.system("mv {} {}".format(jupyterNotebookName, targetPath))
    os.chdir(targetPath)
    os.system("jupyter notebook &")

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
        
        if name+".ipynb" in os.listdir(notesDirectory):
            printLog("note {} already exists".format(name))
            return
        
    elif target == "project":
        projectsRootDirectory = "myprojects"
        projectDirectory = os.path.join(projectsRootDirectory, name)
        jupyterTargetPath = os.path.join(projectDirectory, "src")

        if not os.path.isdir(projectsRootDirectory):
            os.mkdir(projectsRootDirectory)

        if os.path.isdir(projectDirectory):
            printLog("project {} already exists".format(name))
            return
        
        os.mkdir(projectDirectory)
        os.mkdir(jupyterTargetPath)
    else:
        printLog("1. python sup.py note <name>")
        printLog("2. python sup.py project <name>")
        return

    startJupyterNotebook(name, jupyterTargetPath)
    

if __name__ == "__main__":
    main()