#!/usr/bin/python

from common import reader, writer, mapper


def action(line, _writer):
    node_type = line[5].lower()

    if node_type == 'question':
        node_id = line[0]  # 'id' field.
    elif node_type == 'answer':
        node_id = line[6]  # 'parent_id' field. Question id.
    else:
        return  # We ignore non question nor answer nodes.

    post_length = len(line[4])  # Length of 'body' field.

    _writer.writerow([node_id, node_type, post_length])


if __name__ == "__main__":
    mapper(action, reader, writer)
