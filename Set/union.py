'''
.union()

The .union() operator returns the union of a set and the set of elements in an iterable.
Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
Set is immutable to the .union() operation (or | operation).

Example

>>> s = set("Hacker")
>>> print s.union("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(set(['R', 'a', 'n', 'k']))
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(['R', 'a', 'n', 'k'])
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print s.union(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

>>> print s.union({"Rank":1})
set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

>>> s | set("Rank")
set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])'''

'''s = set('taha')
print(s)
b =s.union(['a','m','l'])
print(b)
b =s.union(set(['a','m','l']))
print(b)

b =s.union(set(['aml']))

print(b)
b =s.union(set('aml'))

print(b)

b =s|(set('aml'))

print(b)
b =s|(set('aml'))

print(b)
'''
n = int(input())
france_subscribe =set(map(int ,input().split()))
n2 = int(input())
english_subscribe =set(map(int ,input().split()))

france_english =france_subscribe.union(english_subscribe)
print(len(france_english))






