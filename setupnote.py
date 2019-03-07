import sys
import os
import time

def printLog(msg):
    print("[INFO] {} || {}".format(time.time(), msg))

def main():
    
    projectName = str(sys.argv[1])
    os.system("cp Untitled.ipynb {}.ipynb".format(projectName))
    os.system("mv {}.ipynb notes/".format(projectName))

    os.chdir("notes")    
    os.system("jupyter notebook &")

if __name__ == "__main__":
    main()