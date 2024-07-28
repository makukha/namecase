>>> from namecase import is_snake, to_snake

>>> text = 'Some-Title phrase'
>>> is_snake(text)
False
>>> to_snake(text)
'some_title_phrase'

>>> text = 'Some-Title phrase'

>>> from namecase import is_snake, to_snake
>>> to_snake(text)
'some_title_phrase'
>>> is_snake(to_snake(text))
True

>>> from namecase import is_camel, to_camel
>>> to_camel(text)
'someTitlePhrase'
>>> is_camel(to_camel(text))
True

>>> from namecase import is_pascal, to_pascal
>>> to_pascal(text)
'SomeTitlePhrase'
>>> is_pascal(to_pascal(text))
True

>>> from namecase import is_kebab, to_kebab
>>> to_kebab(text)
'some-title-phrase'
>>> is_kebab(to_kebab(text))
True

>>> from namecase import is_allcaps, to_allcaps
>>> to_allcaps(text)
'SOME_TITLE_PHRASE'
>>> is_allcaps(to_allcaps(text))
True

>>> from namecase import words
>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
'some,really,ME,Ssy,text,wit4,Digits,3Very,Wh3re'

