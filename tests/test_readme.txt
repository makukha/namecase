>>> from caseutil import *

>>> is_snake('My variable-name')
False

>>> to_snake('My variable-name')
'my_variable_name'

>>> is_case('camel', 'myVariableName')
True
>>> to_case(Case.CONST, 'myVariableName')
'MY_VARIABLE_NAME'

>>> words('!some_reallyMESsy text--wit4Digits.3VeryWh3re--')
['some', 'really', 'ME', 'Ssy', 'text', 'wit4', 'Digits', '3Very', 'Wh3re']

>>> '/'.join(words(to_lower('myVariableName')))
'my/variable/name'
>>> '.'.join(words('myVariableName'))
'my.Variable.Name'

