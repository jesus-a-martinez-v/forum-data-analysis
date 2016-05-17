#!/usr/bin/python

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

		author_id = line[3]
		node_type = line[5].lower()

		if node_type == 'question':
			node_id = line[0]  # 'id' field.
		elif node_type in ['answer', 'comment']:
			node_id = line[6]
		else:
			continue

		writer.writerow([node_id, author_id])


mapper()