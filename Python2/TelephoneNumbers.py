__author__ = 'matt'

def fill_dict(l, d, count):
    if not l:
        return {}, count
    item = l.pop(0)
    if not d.has_key(item):
        count += 1
        d[item], count = fill_dict(l, {}, count)
    else:
        d[item], count = fill_dict(l, d[item], count)
    return d, count

input_numbers = ['123',
                 '0123']

n = len(input_numbers)
total_count = 0
numbers_stored = {}
for i in xrange(n):
    telephone = [ch for ch in input_numbers[i]]
    #current_dict = numbers_stored
    for number in telephone:
        numbers_stored, total_count = fill_dict(telephone, numbers_stored, total_count)
        print numbers_stored, total_count
# The number of elements (referencing a number) stored in the structure.
print total_count


numbers_stored = {'count': 0}
for i in xrange(n):
    telephone = input_numbers[i]
    #current_dict = numbers_stored
    for j in range(len(telephone)):
        current = telephone[:(j+1)]
        if not numbers_stored.has_key(current):
            numbers_stored[current] = None
            numbers_stored['count'] += 1
print len(numbers_stored) - 1