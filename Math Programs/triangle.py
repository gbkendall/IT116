# Script Name: triangle.py
# Description: A script to tell you if three side lengths are valid to create a triangle
# Author: Gregory Kendall
# Last Updated: 9.27.2017

import sys

if int(sys.argv[1]) >= int(sys.argv[2]) + int(sys.argv[3]):
    print("False")
elif int(sys.argv[2]) >= int(sys.argv[1]) + int(sys.argv[3]):
    print("False")
elif int(sys.argv[3]) >= int(sys.argv[1]) + int(sys.argv[2]):
    print("False")
else:
    print("True")
