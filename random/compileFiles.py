import sys
import os

def compileFiles(folderIn, fout, num):
    """ Takes multiple files from a directory and compiles
    them into one file and adjusts the time values accordingly.

    Args:
    folderIn - Path of folder with all the messy
    output files.
    fout - Name of output file
    num - Amount of time between each frame. Default is 0.04.
    
    return None"""

    fileOut = open(fout, "w")
    lastXVal = 0
    totalTimeDiff = 0
    for filename in os.listdir(folderIn):
        my_file = os.path.join(folderIn, filename)
        if os.path.isfile(my_file):
            print(my_file)
        
            myFile = open(my_file, "r")
            lines = myFile.readlines()

            for line in lines:
                xVal = float(line.split(' ')[0])
                xVal += totalTimeDiff
                lineString = "%f %s" % (xVal, line.split(' ')[1])
                fileOut.write(lineString)
            
            lastLine = lines[-1]
            lastXVal = float(lastLine.split(' ')[0])
            totalTimeDiff += lastXVal + num
            myFile.close()


def main(argv):
    folderIn = argv[1]
    fout = argv[2]
    if len(argv) == 3:
        compileFiles(folderIn, fout, 0.04)
    else:
        num = float(argv[3])
        compileFiles(folderIn, fout, num)



if __name__ == '__main__':
    main(sys.argv)
