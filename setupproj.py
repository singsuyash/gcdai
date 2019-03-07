import sys
import os
import time

def printLog(msg):
    print("[INFO] {} || {}".format(time.time(), msg))

def main():
    projectName = sys.argv[1]
    projectVenvName = projectName + "Venv"
    myProjectsDirectoryName = "myProjects"
    printLog("python project: {} will be created with virtual env: {}".format(projectName, projectVenvName))
    
    if not os.path.isdir(myProjectsDirectoryName):
        printLog("creating directory {}".format(myProjectsDirectoryName))
        os.mkdir(myProjectsDirectoryName)

    os.chdir(myProjectsDirectoryName)

    if os.path.isdir(projectName):
        printLog("project with name {} already exists".format(projectName))
        return

    os.mkdir(projectName)
    os.chdir(projectName)
    
    os.system("virtualenv {}".format(projectVenvName))
    os.chdir(projectVenvName)
    os.mkdir("src")
    os.mkdir("test")
    os.chdir("../")
    os.chdir("../")
    os.chdir("../")
    printLog("CWD {}".format(os.getcwd()))
    

if __name__ == "__main__":
    main()