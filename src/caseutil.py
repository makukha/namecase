"""
Naming case conventions parsing and converting tool.
"""

from argparse import ArgumentParser
from io import TextIOBase
import re
import sys
from typing import Self


# tokenizer

RX_SIMPLE_SEP = re.compile(r'(_|\W)+')
RX_CASE_SEP1 = re.compile(r'(?P<pre>[a-z][0-9]*)(?P<post>[A-Z])')
RX_CASE_SEP2 = re.compile(r'(?P<pre>[A-Z][0-9]*)(?P<post>[A-Z][0-9]*[a-z])')

def words(text: str) -> str:
    values = RX_SIMPLE_SEP.sub(',', text)
    values = RX_CASE_SEP1.sub(r'\g<pre>,\g<post>', values)
    values = RX_CASE_SEP2.sub(r'\g<pre>,\g<post>', values)
    return values.strip(',')


# cases

UPPER = r'(?:[A-Z0-9]+)'
LOWER = r'(?:[a-z0-9]+)'
TITLE = rf'(?:[0-9]*[A-Z]{LOWER}?)'

RX_SNAKE = re.compile(f'{LOWER}(_{LOWER})*')
RX_CAMEL = re.compile(f'{LOWER}{TITLE}*')
RX_PASCAL = re.compile(f'{TITLE}+')
RX_KEBAB = re.compile(f'{LOWER}(-{LOWER})*')
RX_ALLCAPS = re.compile(f'{UPPER}(_{UPPER})*')
RX_TITLE = re.compile(f'{TITLE}( {TITLE})*')

# snake case

def is_snake(text: str) -> bool:
    return True if RX_SNAKE.fullmatch(text) else False

def to_snake(text: str) -> str:
    return words(text).lower().replace(',', '_')

# camel case

def is_camel(text: str) -> bool:
    return True if RX_CAMEL.fullmatch(text) else False

def to_camel(text: str) -> str:
    wrds = words(text).split(',')
    if len(wrds) == 0:
        value = ''
    else:
        value = ''.join([wrds[0].lower(), *(w.title() for w in wrds[1:])])
    return value

# pascal case

def is_pascal(text: str) -> bool:
    return True if RX_PASCAL.fullmatch(text) else False

def to_pascal(text: str) -> str:
    return ''.join(w.title() for w in words(text).split(','))

# kebab case

def is_kebab(text: str) -> bool:
    return True if RX_KEBAB.fullmatch(text) else False

def to_kebab(text: str) -> str:
    return words(text).lower().replace(',', '-')

# all caps case

def is_allcaps(text: str) -> bool:
    return True if RX_ALLCAPS.fullmatch(text) else False

def to_allcaps(text: str) -> str:
    return words(text).upper().replace(',', '_')

# title case

def is_title(text: str) -> bool:
    return True if RX_TITLE.fullmatch(text) else False

def to_title(text: str) -> str:
    return ' '.join(w.title() for w in words(text).split(','))


# all cases

CASES = {
    'allcaps': to_allcaps,
    'camel': to_camel,
    'kebab': to_kebab,
    'pascal': to_pascal,
    'snake': to_snake,
    'title': to_title,
}


# cli

parser = ArgumentParser(prog='caseutil', description=__doc__)
parser.add_argument('text', default=sys.stdin, nargs='?')
parser.add_argument('-c', '--case', choices=CASES.keys(), required=True)


def main() -> None:
    args = parser.parse_args()
    lines = (
        args.text.readlines()
        if isinstance(args.text, TextIOBase)
        else args.text.splitlines()
    )
    values = [CASES[args.case](line) for line in lines]
    print(*values, sep='\n')


if __name__ == '__main__':
    main()
