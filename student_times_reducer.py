#!/usr/bin/python
import sys
import csv


def reducer():
	reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    current_student_id = None  # Student id being processed.
    current_hour = None  # Hour being processed.
    current_count = 0  # Count of the hour being processed.
    max_count = 0  # Count of the hour with most occurrences for this student.
    max_hours = set([])  # Hours that appear 'max_count' times for this student's rows. 

    for line in reader:
        student_id = line[0]
        hour_of_day = int(line[1])

        if current_student_id and current_student_id == student_id:
            # If this line hour is the same being processed, then we increment the counter.
            if current_hour and current_hour == hour_of_day:
        	   current_count += 1
            else:
            # If this line hour isn't the same being processed, then...
                if current_count > max_count:
                    # If the count for the current hour is higher than the max, then replace both the max_count and the max_hours.
                    max_count = current_count
                    max_hours = set([current_hour])
                elif current_count == max_count:
                    # If there's a tie, then we store the current_hour together with the previously found max_hour.
                    max_hours.add(hour_of_day)
                
                current_hour = hour_of_day
                current_count = 1

        else:
            # When the student being processed changes, then we must print the results found until this point.
            for hour in max_hours:
            	writer.writerow([current_student_id, hour])

        	current_student_id = student_id
        	current_count = 1
            current_hour = hour_of_day
            max_count = 1
        	max_hours = set([hour_of_day])

    for hour in max_hours:
        writer.writerow([current_student_id, hour])

reducer()