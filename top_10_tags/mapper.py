#!/usr/bin/python

from common import reader, writer, mapper


def action(line, _writer):
    node_type = line[5].lower()

    if node_type == 'question':
        tags = line[2].split(' ')

        for tag in tags:
            _writer.writerow([tag, '1'])


if __name__ == "__main__":
    mapper(action, reader, writer)
