from collections import Counter
from collections import defaultdict
from collections import namedtuple
from datetime import date

ls = '111122223113123221323141412123131312312'
print(Counter(ls))
print(Counter(ls).most_common(1))



ls = 'aaabbcsdadabbabbcbabsdadhadhadjhsad'
print(Counter(ls))
print(Counter(ls).most_common(1))

d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['correct'])
print(d['noPresent'])

Dog = namedtuple('Dog', ['age', 'breed', 'name'])

fido = Dog(age=5, breed='retreiver', name='fido')
print(fido)
print(fido.age)
print(fido[0])

born = date(1993, 10, 19)
today = date.today()
age = today - born
print((age.days - 5)/365)