#!/usr/bin/env python
import os.path

#Author: Sumit Joshi
#date:5/12/2015
# Log File Search Script
# This Script is useful for searching specific keyword in log files. For specific keyword it returns matching lines.


print "*******************************************************"
print ""
print ""
print "Welcome to the Python Log Search Program"
print "Search log files with specific keywords..."
print ""
print ""
print "*******************************************************"
print ""

log_file=raw_input("Enter the path of the log file that you want to read  ")
print log_file

if os.path.isfile(log_file):
        keyword=raw_input('Enter the keywords that you want to search in log file with space ').split(" ")
        #for storing final log lines
        final=[]
        fd=open(log_file,"r")

        for line in fd.readlines():
                for item in keyword:
                        if item in line:
                                final.append(line)
                                final.append('')
        if len(final)==0:
                print "No matching lines found in", log_file
        else:
                print 'Found matching lines in ', log_file
                for log_line in final:
                        print log_line
else:
        print 'Please enter valid log file name'
