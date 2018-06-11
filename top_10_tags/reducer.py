#!/usr/bin/python

from common import reader, writer


def reducer():
    top_10 = []
    current_tag = None
    current_tag_count = 0
    for line in reader:
        tag = line[0]
        count = int(line[1])

        if not current_tag:
            current_tag = tag

        if current_tag != tag:
            if len(top_10) < 10:
                top_10.append((current_tag, current_tag_count))
                top_10 = sorted(top_10, key=lambda p: p[1], reverse=True)
            else:
                if current_tag_count > top_10[-1][1]:
                    top_10[-1] = (current_tag, current_tag_count)
                    top_10 = sorted(top_10, key=lambda p: p[1], reverse=True)

            current_tag = tag
            current_tag_count = 0

        current_tag_count += count

    if len(top_10) < 10:
        top_10.append((current_tag, current_tag_count))
        top_10 = sorted(top_10, key=lambda p: p[1], reverse=True)
    else:
        if current_tag_count > top_10[-1][1]:
            top_10[-1] = (current_tag, current_tag_count)
            top_10 = sorted(top_10, key=lambda p: p[1], reverse=True)

    for elem in top_10:
        writer.writerow([elem[0], elem[1]])


if __name__ == "__main__":
    reducer()
