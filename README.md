# caseutil
[![license](https://img.shields.io/github/license/makukha/caseutil.svg)](https://github.com/makukha/caseutil/blob/main/LICENSE)
[![Coverage Status](https://raw.githubusercontent.com/makukha/caseutil/0.5.3/docs/img/coverage-badge.svg)](https://github.com/makukha/caseutil)
[![pypi](https://img.shields.io/pypi/v/caseutil.svg)](https://pypi.python.org/pypi/caseutil)
[![versions](https://img.shields.io/pypi/pyversions/caseutil.svg)](https://pypi.org/project/caseutil)

Case convert and verify for Python: snake_case, camelCase, kebab-case, and more.


## Features

* Verify and convert between most popular cases
* Custom separators: `'my.variable.name'`, `'my/variable/name'`
* Command line mode: `caseutil`
* Pure Python 2.7 to 3.13+
* No dependencies
* 100% test coverage


## Supported Cases

| case name                 | func         | example          |
|---------------------------|--------------|------------------|
| Snake case                | `to_snake`   | my_variable_name |
| All caps, screaming snake | `to_allcaps` | MY_VARIABLE_NAME |
| Camel case                | `to_camel`   | myVariableName   |
| Pascal case               | `to_pascal`  | MyVariableName   |
| Kebab case, spinal case   | `to_kebab`   | my-variable-name |
| Lower space-separated     | `to_lower`   | my variable name |
| Upper space-separated     | `to_upper`   | MY VARIABLE NAME |
| Title space-separated     | `to_title`   | My Variable Name |


## Installation

```bash
$ pip install caseutil
```

## Quick Start

Call `is_*` to verify case format, and `to_*` to convert to specific case:
```doctest
>>> from caseutil import *
>>> is_snake('My variable-name')
False
>>> to_snake('My variable-name')
'my_variable_name'
```

Use as command line tool, pass multiple values in argument or stdin:
```bash
$ caseutil -c allcaps "hi there"
HI_THERE
$ echo "hi_there\nsee you" | python -m caseutil -c camel
hiThere
seeYou
```


## Universal Functions

Use functions `is_case()` and `to_case()` to deal with arbitrary case:
```doctest
>>> is_case('camel', 'myVariableName')
True
>>> to_case(Case.ALLCAPS, 'myVariableName')
'MY_VARIABLE_NAME'
```

All supported cases are gathered in `Case` enum:
```python
class Case(StrEnum):
    ALLCAPS = 'allcaps'
    CAMEL = 'camel'
    KEBAB = 'kebab'
    LOWER = 'lower'
    PASCAL = 'pascal'
    SNAKE = 'snake'
    TITLE = 'title'
    UPPER = 'upper'
```


## Tokenization

Word separators are non-word characters including underscore, and places where text case is changed from lower to upper. Digits are not treated as separators. For more details, see this example and unit tests.

```doctest
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']
```

## Custom Separators

For custom separators, use `words()` function:
```doctest
>>> '/'.join(words(to_lower('myVariableName')))
'my/variable/name'
>>> '.'.join(words('myVariableName'))
'my.Variable.Name'
```


## Unicode

Only ASCII names are supported. Unicode support is planned.


---


## 🛠 Developer's Corner

### Develop on Mac OS X

Requires Docker and Homebrew.

```bash
git clone https://github.com/makukha/caseutil.git
brew install go-task
task init
```

Testing:

```bash
task test
```

### Plans

* Add more test, explore edge cases
* Add Unicode support (write tests)
* Add more cases
