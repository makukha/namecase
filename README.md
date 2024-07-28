# namecase
[![license](https://img.shields.io/github/license/makukha/namecase.svg)](https://github.com/makukha/namecase/blob/main/LICENSE)
[![pypi](https://img.shields.io/pypi/v/namecase.svg)](https://pypi.python.org/pypi/namecase)
[![versions](https://img.shields.io/pypi/pyversions/namecase.svg)](https://github.com/pydantic/pydantic)

**Naming case conventions parsing and converting tool.**

Small and clean, fully typed, zero dependency pure Python 2.7 to 3.13 and probably above.

The package supports detection and conversion between cases:

* snake_case
* camelCase
* PascalCase
* kebab-case
* ALL_CAPS_CASE (aka SCREAMING_SNAKE_CASE)
* Title Case

and more to be added.


## Usage

```doctest
>>> from namecase import is_snake, to_snake

>>> text = 'Some-Title phrase'
>>> is_snake(text)
False
>>> to_snake(text)
'some_title_phrase'
```

### Command line tool

```bash
$ namecase --case allcaps "hi there"
HI_THERE
$ echo "hi_there\nsee you" | python -m namecase -c camel
hiThere
seeYou
```

### Supported cases

```doctest
>>> text = 'Some-Title phrase'
```

#### snake_case
```doctest
>>> from namecase import is_snake, to_snake
>>> to_snake(text)
'some_title_phrase'
>>> is_snake(to_snake(text))
True
```

#### camelCase
```doctest
>>> from namecase import is_camel, to_camel
>>> to_camel(text)
'someTitlePhrase'
>>> is_camel(to_camel(text))
True
```

#### PascalCase
```doctest
>>> from namecase import is_pascal, to_pascal
>>> to_pascal(text)
'SomeTitlePhrase'
>>> is_pascal(to_pascal(text))
True
```

#### kebab-case
```doctest
>>> from namecase import is_kebab, to_kebab
>>> to_kebab(text)
'some-title-phrase'
>>> is_kebab(to_kebab(text))
True
```

#### ALL_CAPS_CASE
```doctest
>>> from namecase import is_allcaps, to_allcaps
>>> to_allcaps(text)
'SOME_TITLE_PHRASE'
>>> is_allcaps(to_allcaps(text))
True
```

#### Title Case
```doctest
>>> from namecase import is_title, to_title
>>> to_title(text)
'Some Title Phrase'
>>> is_title(to_title(text))
True
```

### Separators

Phrase separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators.

```doctest
>>> from namecase import words
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
'some,really,ME,Ssy,text,wit4,Digits,3Very,Wh3re'
```

### Unicode

Only ASCII names are supported. Unicode support is planned.


## Development

### Mac OS X

Requires Docker and Homebrew.

```bash
git clone https://github.com/makukha/namecase.git
brew install go-task
task init
```

Testing:

```bash
task test
```

## Plans

* Add more test, explore edge cases
* Add Unicode support (write tests)
* Add more cases
