#!/usr/bin/python

from datetime import datetime

from common import reader, writer, mapper


def action(line, _writer):
    student_id = line[3]
    date = line[8].split('.')[0]  # We don't use the offset.
    hour_of_day = datetime.strptime(date, "%Y-%m-%d %H:%M:%S").time().hour

    _writer.writerow([student_id, hour_of_day])


if __name__ == "__main__":
    mapper(action, reader, writer)
