import sys
import os
import time

def printLog(msg):
    print("[INFO] {} || {}".format(time.time(), msg))

def main():
    projectName = sys.argv[1]
    myProjectsDirectoryName = "myProjects"
    printLog("python project: {} will be created".format(projectName))
    
    if not os.path.isdir(myProjectsDirectoryName):
        printLog("creating directory {}".format(myProjectsDirectoryName))
        os.mkdir(myProjectsDirectoryName)

    os.chdir(myProjectsDirectoryName)

    if os.path.isdir(projectName):
        printLog("project with name {} already exists".format(projectName))
        return

    os.mkdir(projectName)
    os.chdir(projectName)
    
    os.mkdir("src")
    os.mkdir("test")
    os.chdir("../")
    os.chdir("../")
    
    os.system("cp Untitled.ipynb {}.ipynb".format(projectName))
    os.system("mv {}.ipynb {}/{}/src/".format(projectName, myProjectsDirectoryName, projectName))

    printLog("CWD {}".format(os.getcwd()))
    os.chdir("{}/{}/src/".format(myProjectsDirectoryName, projectName))
    os.system("jupyter notebook &")
    

if __name__ == "__main__":
    main()