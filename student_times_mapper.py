#!/usr/bin/python

from datetime import datetime
import sys
import csv


def mapper():
		reader = csv.reader(sys.stdin, delimiter='\t')
    	writer = csv.writer(sys.stdout, delimiter='\t')

    	header = True

    	for line in reader:
    		if header:
    			header = False
    			continue
    			
    		student_id = line[3]
    		date = line[8].split('.')[0]  # We don't use the offset.
    		hour_of_day = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").time().hour

    		writer.writerow([student_id, hour_of_day])

mapper()