#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import getopt
import re
import os

def main(argv):
    trackfile = ''
    elffile = ''
    try:
        opts, args = getopt.getopt(argv, "t:e:", ["trackfile=", "elffile="])
    except getopt.GetoptError:
        print('Error: backtrack.py -t <trackfile> -e <elffile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-t", "--trackfile"):
            track_file = arg
        elif opt in ("-e", "--elffile"):
            elffile = arg

    for line in open(track_file):
        pattern = r"(\[.*?\])";
        results = re.findall(pattern,line ,re.M)
        if(len(results) == 2):
            addr = results[1]
            addr = addr.replace('[','').replace(']','')
            cmd = "addr2line -e " + elffile + " " + addr
            os.system(cmd)

if __name__ == "__main__":
    main(sys.argv[1:])