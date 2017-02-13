#!/usr/bin/env python3
from argparse import ArgumentParser

import markdown
import re


def parse_args():
    parser = ArgumentParser()
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
    return text.strip().replace('\n', ' ').replace('<p>', '').replace('</p>', '')

def to_deck(data):
    for card in to_md(data.strip()).split('<hr>'):
        match = re.search(
            '<blockquote>(?P<question>.*)</blockquote>(?P<answer>.*)', card, flags=re.S)
        # print('%r\n%r\n\n' % (card, match.groupdict()))
        yield (
            clean(match.groupdict()['question']),
            clean(match.groupdict()['answer'])
        )

if __name__ == '__main__':
    args = parse_args()
    for filename in args.files:
        with open(filename, 'r') as f:
            with open(filename.replace('.cards.md', '.deck.txt'), 'w') as fw:
                for q, a in to_deck(f.read()):
                    fw.write('%s\t%s\n' % (q, a))

