import os
import re
import sys
import textwrap

from os import path

patterns = [
    (re.compile(p), r) for p, r in [
        (r'[ \t]+', ' '),
        (r'\n\n+', '\n\n'),
        (r'\n[ \t]+', '\n'),
    ]
]


def reformat(source, dest):
    print(f'{source} -> {dest}')

    with open(source, encoding='latin_1') as f:
        contents = f.read()

    for pattern, replacement in patterns:
        contents = pattern.sub(replacement, contents)

    contents = '\n'.join(
        textwrap.fill(line, width=80) for line in contents.splitlines()
    )

    with open(dest, 'w') as f:
        f.write(contents)


def main(source, target):
    for root, dirs, files in os.walk(source):
        for name in files:
            src = path.join(root, name)
            dest = path.join(target, name)
            reformat(src, dest)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
