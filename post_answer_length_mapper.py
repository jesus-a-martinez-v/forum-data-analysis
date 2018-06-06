#!/usr/bin/python

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    header = True

    for line in reader:
        if header:  # Ignore header from now on.
            header = False
            continue

        node_type = line[5].lower()

        if node_type == 'question':
            node_id = line[0]  # 'id' field.
        elif node_type == 'answer':
            node_id = line[6]  # 'parent_id' field. Question id.
        else:
            continue  # We ignore non question nor answer nodes.

        post_length = len(line[4])  # Length of 'body' field.

        writer.writerow([node_id, node_type, post_length])


mapper()
