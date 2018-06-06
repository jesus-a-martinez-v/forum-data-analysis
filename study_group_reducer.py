#!/usr/bin/python

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t')

    current_node = None
    students_in_node = []

    for line in reader:
        node = line[0]
        student = line[1]

        if not current_node:
            current_node = node

        if current_node != node:
            writer.writerow([current_node, str(students_in_node)])
            current_node = node
            students_in_node = []

        students_in_node.append(student)

    writer.writerow([current_node, str(students_in_node)])


reducer()
