# namecase

Naming case conventions parsing and converting tool.

Small and clean, fully typed, zero dependency pure Python 2.7 to 3.13 and probably above.

---
The package supports detection and conversion between cases: snake_case, camelCase, PascalCase, kebab-case, ALL_CAPS_CASE (aka SCREAMING_SNAKE_CASE).

All methods are cached for better performance.


## Usage

```doctest
>>> from namecase import Case
>>> text = Case('Some-Title phrase')
>>> isinstance(text, str)
True
>>> text.is_snake()
False
>>> text.to_snake()
'some_title_phrase'
```

### CLI

```bash
$ namecase --to=allcaps "hi there"
# HI_THERE
$ echo "hi_there\nsee you" | python -m namecase -t camel
# hiThere
# seeYou
```

### Supported cases

#### snake_case
```doctest
>>> text = Case('Some-Title phrase')
>>> text.to_snake()
'some_title_phrase'
>>> text.to_snake().is_snake()
True
```

#### camelCase
```doctest
>>> text = Case('Some-Title phrase')
>>> text.to_camel()
'someTitlePhrase'
>>> text.to_camel().is_camel()
True
```

#### PascalCase
```doctest
>>> text = Case('Some-Title phrase')
>>> text.to_pascal()
'SomeTitlePhrase'
>>> text.to_pascal().is_pascal()
True
```

#### kebab-case
```doctest
>>> text = Case('Some-Title phrase')
>>> text.to_kebab()
'some-title-phrase'
>>> text.to_kebab().is_kebab()
True
```

#### ALL_CAPS_CASE
```doctest
>>> text = Case('Some-Title phrase')
>>> text.to_allcaps()
'SOME_TITLE_PHRASE'
>>> text.to_allcaps().is_allcaps()
True
```

### Separators

Phrase separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators.

```doctest
>>> phrase = Case('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
>>> phrase.words()
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
* Add GitHub Pages docs
* Add release notes
