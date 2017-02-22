#!/usr/bin/env python3
from argparse import ArgumentParser

import markdown

import sys


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-n', '--dry-mode', action='store_true')
    parser.add_argument('files', nargs='+')
    return parser.parse_args()


to_md = markdown.Markdown(
    output_format='html5',
    extensions=[
        "markdown.extensions.fenced_code",
        "markdown.extensions.codehilite",
        "markdown.extensions.tables",
    ],
    extension_configs={
        'markdown.extensions.codehilite': {'noclasses': True},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
).convert


def clean(text):
    return to_md(text.strip()).replace('<p>', '').replace('</p>', '')
    # .replace('\n', ' ')


def to_deck(data):
    q, a = '', ''
    for line in data.strip().split('\n'):
        if line.startswith('>') and not a:
            q += line.replace('> ', '')
        elif not line.startswith('>'):
            a += line
        elif line.startswith('>') and a:
            yield clean(q), clean(a)
            q, a = '', ''
            q += line.replace('> ', '')
    yield clean(q), clean(a)

if __name__ == '__main__':
    args = parse_args()
    with open('all.deck.txt', 'w') as all_deck:
        for filename in args.files:
            with \
                open(filename, 'r') as input_file, \
                open(filename.replace('.cards.md', '.deck.txt'), 'w') as this_deck \
            :
                for q, a in to_deck(input_file.read()):
                    tsv_line = '%s\t%s\n' % (q, a)
                    if args.dry_mode:
                        sys.stdout.write(tsv_line)
                    else:
                        this_deck.write(tsv_line)
                        all_deck.write(tsv_line)
