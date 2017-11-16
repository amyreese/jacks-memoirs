import os
import shutil
import sys

from collections import defaultdict
from os import path
from prettytable import PrettyTable


def sort_key(value):
    keyname, size = value
    return size


def main(source, target):
    all_stats = defaultdict(list)
    for root, dirs, files in os.walk(source):
        for name in files:
            keyname = name.lower()
            if not keyname.endswith('doc'):
                continue

            fullpath = path.join(root, name)
            with open(fullpath, encoding='latin_1') as f:
                data = f.read()
                size = len(data)
                all_stats[keyname].append((fullpath, size))

    table = PrettyTable()
    for key, stats in all_stats.items():
        stats = sorted(stats, key=sort_key, reverse=True)
        fullpath, size = stats[0]
        table.add_row([fullpath, key, size])

        shutil.copy(fullpath, path.join(target, key))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
