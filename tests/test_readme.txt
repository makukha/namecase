>>> from namecase import Case
>>> text = Case('Some-Title phrase')
>>> isinstance(text, str)
True
>>> text.is_snake()
False
>>> text.to_snake()
'some_title_phrase'

>>> text = Case('Some-Title phrase')
>>> text.to_snake()
'some_title_phrase'
>>> text.to_snake().is_snake()
True

>>> text = Case('Some-Title phrase')
>>> text.to_camel()
'someTitlePhrase'
>>> text.to_camel().is_camel()
True

>>> text = Case('Some-Title phrase')
>>> text.to_pascal()
'SomeTitlePhrase'
>>> text.to_pascal().is_pascal()
True

>>> text = Case('Some-Title phrase')
>>> text.to_kebab()
'some-title-phrase'
>>> text.to_kebab().is_kebab()
True

>>> text = Case('Some-Title phrase')
>>> text.to_allcaps()
'SOME_TITLE_PHRASE'
>>> text.to_allcaps().is_allcaps()
True

>>> phrase = Case('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
>>> phrase.words()
'some,really,ME,Ssy,text,wit4,Digits,3Very,Wh3re'

