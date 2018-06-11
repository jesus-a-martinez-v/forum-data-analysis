#!/usr/bin/python

from common import reader, writer, mapper


def action(line, _writer):
    author_id = line[3]
    node_type = line[5].lower()

    if node_type == 'question':
        node_id = line[0]  # 'id' field.
    elif node_type in ['answer', 'comment']:
        node_id = line[6]
    else:
        return

    _writer.writerow([node_id, author_id])


if __name__ == "__main__":
    mapper(action, reader, writer)

