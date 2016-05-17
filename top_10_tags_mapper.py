#!/usr/bin/python

import sys
import csv


def mapper():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t')

	for line in reader:

		header = True

		if header:
			header = False
			continue

		node_type = line[5].lower()

		if node_type == 'question':
			tags = line[2].split(' ')

			for tag in tags:
				writer.writerow([tag, '1'])


mapper()