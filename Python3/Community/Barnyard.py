"""
The Barnyard

Problem description:
In your barnyard, you have rabbits, chickens, cows, pegasi and demons.
You gather your animals and you count the heads, the horns, the legs,
the wings and the eyes.
Every animal has one head.
The rabbits have four legs and two eyes.
The chickens have two legs, two wings and two eyes.
The cows have two horns, four legs and two eyes.
The pegasi have four legs, two wings and two eyes.
The demons have four horns, four legs, two wings and four eyes.
You are given a list of the species that you have and the total
number of heads, horns, legs, wings and eyes.
You must print the number of animals of each species
that are in your barnyard (in the same order that they were given).

"""

import numpy as np


class Barnyard(object):

    def __init__(self, a, p):
        self.solution = None
        self.norms = {"rabbits": {"heads": 1, "legs": 4, "eyes": 2,
                                  "horns": 0, "wings": 0},
                      "chickens": {"heads": 1, "legs": 2, "eyes": 2,
                                   "wings": 2, "horns": 0},
                      "cows": {"heads": 1, "horns": 2, "legs": 4,
                               "eyes": 2, "wings": 0},
                      "pegasi": {"heads": 1, "legs": 4, "wings": 2,
                                 "eyes": 2, "horns": 0},
                      "demons": {"heads": 1, "horns": 4, "legs": 4,
                                 "wings": 2, "eyes": 4}}
        self.a = a
        self.p = p

        v = list()
        m = list()
        for part, val in self.p.items():
            v.append(val)
            l = list()
            for animal in self.a:
                l.append(self.norms[animal.lower()][part])
            m.append(l)
        self.m = np.array(m)
        self.v = np.array(v)

    def __repr__(self):
        return "{}\n{}\n{}\n{}\n".format(self.a, self.p, self.m, self.v)

    def solve(self):
        sol = np.linalg.solve(self.m, self.v)
        self.solution = [int(i) for i in sol]

    def print_answer(self):
        for key, val in zip(self.a, self.solution):
            print('{} {}'.format(key, val))


def localtest():
    animals = ['Rabbits', 'Chickens']
    parts = {'heads': 5, 'legs': 14}

    barnyard = Barnyard(animals, parts)
    print(barnyard)
    barnyard.solve()
    assert sorted(barnyard.solution) == sorted(np.array([2, 3]))
    barnyard.print_answer()


def codingame():
    n = int(input())
    list_of_animals = input().split()
    parts_dict = {}
    for i in range(n):
        p, num = input().split()
        print(p, num)
        num = int(num)
        parts_dict[p.lower()] = num

    b = Barnyard(list_of_animals, parts_dict)
    b.solve()
    b.print_answer()


if __name__ == '__main__':
    codingame()
