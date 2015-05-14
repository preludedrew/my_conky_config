#!/usr/bin/python

from subprocess import PIPE
import subprocess
import getopt, sys

def get_packages(get_total):

    output = subprocess.Popen(['pacman', '-Sup'], stdout=PIPE, stderr=PIPE)
    split = output.communicate()[0].split("\n") 

    update_num = 0
    for line in split:
        if line and line != ":: Starting full system upgrade...":
	    splitLine = line.split("/")

	    if update_num < 5 and not get_total:
	        print splitLine[len(splitLine) - 1]

	    update_num += 1

    if get_total:
        print update_num


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "t", ["total"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        show_usage()
        sys.exit(2)

    get_total = False

    for o, a in opts:
        if o == "-t":
            get_total = True

    get_packages(get_total)

if __name__ == "__main__":
    main()
