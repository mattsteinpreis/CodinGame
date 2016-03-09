__author__ = 'matt'

import itertools


def fill_dict(l, d):
    l = [ch for ch in l]
    if not l:
        return {}
    item = l.pop(0)
    if item not in d:
        d[item] = fill_dict(l, {})
    else:
        d[item] = fill_dict(l, d[item])
    return d


def get_word_list(letters):
    l = len(letters)
    words = []
    for i in xrange(l):
        it = itertools.permutations(letters, i+1)
        words.extend([''.join(w) for w in it])
    return set(words)


def point_values():
    p = [('eaionrtlsu', 1),
         ('dg', 2),
         ('bcmp', 3),
         ('fhvwy', 4),
         ('k', 5),
         ('jx', 8),
         ('qz', 10)]
    d = {}
    for tup in p:
        for ch in tup[0]:
            d[ch] = tup[1]
    return d


def word_score(w, d):
    points = [d[ch] for ch in w]
    return sum(points)


letter_points = point_values()
word_dict = {}
simple_dict = {}
n = int(raw_input())
for ii in xrange(n):
    word = raw_input()
    word_dict = fill_dict(word, word_dict)
    simple_dict[word] = ii

letters_given = raw_input()
possible_words = get_word_list(letters_given)

best_score = 0
best_index = -1
best_word = ''
for word in possible_words:
    if word in simple_dict:
        score = word_score(word, letter_points)
        id = simple_dict[word]
        if score > best_score or (score = best_score and id < best_index):
            best_score = score
            best_word = word
            best_index = id
print best_word