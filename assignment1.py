__author__ = 'cs'

import sys


def main():

    writeFirst20Lines(sys.argv[1])



def writeFirst20Lines(filename):
    file = open(filename)
    resultList = file.readlines()

    #print resultList
    print str(len(resultList))

    f = open('ass1.txt','w')

    counter = 0
    for item in resultList:
        if counter < 20:
            counter += 1
            f.write("%s" % item)
        else:
            break



if __name__ == '__main__':
    main()