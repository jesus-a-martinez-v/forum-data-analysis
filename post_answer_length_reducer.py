#!/usr/bin/python

import sys
import csv

def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
	writer = csv.writer(sys.stdout, delimiter='\t')
	
	current_node_id = None
	current_question_length = 0
	answer_length_sum = 0
	answer_length_count = 0

	for line in reader:
		node_id = line[0]
		node_type = line[1]
		post_length = float(line[2])

		if not current_node_id:  # If this is the first node processed, then set it as the current node.
			current_node_id = node_id

		if current_node_id != node_id:
			if answer_length_count == 0:
				answer_length_mean = 0
			else:
				answer_length_mean = answer_length_sum / answer_length_count

			writer.writerow([current_node_id, int(current_question_length), answer_length_mean])
			
			current_node_id = node_id
			current_question_length = 0
			answer_length_sum = 0
			answer_length_count = 0

		# If this node is of 'question' type, we'll store the length of the question.
		if node_type == 'question':
			current_question_length = post_length
		# Otherwise, it's an 'answer' node and we'll increment both the answer_length sum and count.
		else:
			answer_length_sum += post_length
			answer_length_count += 1

	if answer_length_count == 0:
		answer_length_mean = 0
	else:
		answer_length_mean = answer_length_sum / answer_length_count
	writer.writerow([current_node_id, int(current_question_length), answer_length_mean])


reducer()