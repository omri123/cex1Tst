import subprocess
import difflib

testsFolderPath = "//cs//usr//omribloch//Desktop//c//ex1//myTests//"
programPath = "//cs//usr//omribloch//Desktop//c//ex1//StringChange"

for i in range(1,12):

    inputFilePath = testsFolderPath + "string" + str(i) + ".txt"
    outputFilePath = testsFolderPath + "string" + str(i) + "out.txt"
    compareFilePath = testsFolderPath + "string" + str(i) +".out"

    inputFile = open(inputFilePath)
    outputFile = open(outputFilePath, 'w+')

    subprocess.call(programPath, stdin = inputFile, stdout = outputFile)

    cmpFile = open(compareFilePath)
    outputFile.close()
    outputFile = open(outputFilePath)
    #inputFile.close()

    out_str = outputFile.read()
    cmp_str = cmpFile.read()
    print("\n \n \ntester " + str(i))
    print("algo output = " + out_str)
    print("cmp File =    " + cmp_str)

    out_str_lines = out_str.splitlines()
    cmp_str_lines = cmp_str.splitlines()

    d = difflib.Differ()
    diff = d.compare(out_str_lines, cmp_str_lines)
    print '\n'.join(diff)