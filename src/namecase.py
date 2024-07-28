"""
Naming case conventions parsing and converting tool.
"""

from argparse import ArgumentParser
from functools import cache
from io import TextIOBase
import re
import sys
from typing import Self


CASES = ('allcaps', 'camel', 'kebab', 'pascal', 'snake')

UPPER = r'(?:[A-Z0-9]+)'
LOWER = r'(?:[a-z0-9]+)'
TITLE = rf'(?:[0-9]*[A-Z]{LOWER}?)'

RX_SNAKE = re.compile(f'{LOWER}(_{LOWER})*')
RX_CAMEL = re.compile(f'{LOWER}{TITLE}*')
RX_PASCAL = re.compile(f'{TITLE}+')
RX_KEBAB = re.compile(f'{LOWER}(-{LOWER})*')
RX_ALLCAPS = re.compile(f'{UPPER}(_{UPPER})*')


class Case(str):
    @cache
    def words(self) -> str:
        return tokenize(self)

    # snake case

    @cache
    def is_snake(self) -> bool:
        return True if RX_SNAKE.fullmatch(self) else False

    @cache
    def to_snake(self) -> Self:
        value = self.words().lower().replace(',', '_')
        return Case(value)

    # camel case

    @cache
    def is_camel(self) -> bool:
        return True if RX_CAMEL.fullmatch(self) else False

    @cache
    def to_camel(self) -> Self:
        words = self.words().split(',')
        if len(words) == 0:
            value = ''
        else:
            value = ''.join([words[0].lower(), *(w.title() for w in words[1:])])
        return Case(value)

    # pascal case

    @cache
    def is_pascal(self) -> bool:
        return True if RX_PASCAL.fullmatch(self) else False

    @cache
    def to_pascal(self) -> Self:
        words = self.words().split(',')
        if len(words) == 0:
            value = ''
        else:
            value = ''.join(w.title() for w in words)
        return Case(value)

    # kebab case

    @cache
    def is_kebab(self) -> bool:
        return True if RX_KEBAB.fullmatch(self) else False

    @cache
    def to_kebab(self) -> Self:
        value = self.words().lower().replace(',', '-')
        return Case(value)

    # all caps case

    @cache
    def is_allcaps(self) -> bool:
        return True if RX_ALLCAPS.fullmatch(self) else False

    @cache
    def to_allcaps(self) -> Self:
        value = self.words().upper().replace(',', '_')
        return Case(value)


# tokenizer

RX_SIMPLE_SEP = re.compile(r'(_|\W)+')
RX_CASE_SEP1 = re.compile(r'(?P<pre>[a-z][0-9]*)(?P<post>[A-Z])')
RX_CASE_SEP2 = re.compile(r'(?P<pre>[A-Z][0-9]*)(?P<post>[A-Z][0-9]*[a-z])')


def tokenize(text: str) -> str:
    words = RX_SIMPLE_SEP.sub(',', text)
    words = RX_CASE_SEP1.sub(r'\g<pre>,\g<post>', words)
    words = RX_CASE_SEP2.sub(r'\g<pre>,\g<post>', words)
    return words.strip(',')


# cli

parser = ArgumentParser(prog='namecase', description=__doc__)
parser.add_argument('text', default=sys.stdin, nargs='?')
parser.add_argument('-t', '--to', choices=CASES, required=True)


def main() -> None:
    args = parser.parse_args()
    to_case = lambda t: getattr(Case(t), f'to_{args.to}')()
    if isinstance(args.text, TextIOBase):
        lines = args.text.readlines()
    else:
        lines = [args.text]
    values = [to_case(line) for line in lines]
    print(*values, sep='\n')


if __name__ == '__main__':
    main()
