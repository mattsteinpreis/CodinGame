__author__ = 'matt'


def get_card_rank(c):
    if c == 'J':
        return 11
    if c == 'Q':
        return 12
    if c == 'K':
        return 13
    if c == 'A':
        return 14
    return int(c)


def play_hand(s1, s2, pile1 = None, pile2 = None):
    if pile1 is None:
        pile1 = []
    if pile2 is None:
        pile2 = []
    try:
        c1 = s1.pop(0)
        c2 = s2.pop(0)
    except IndexError:
        return "PAT"
    pile1.append(c1)
    pile2.append(c2)
    if c1 > c2:
        s1.extend(pile1)
        s1.extend(pile2)
        winner = '1'
    elif c2 > c1:
        s2.extend(pile1)
        s2.extend(pile2)
        winner = '2'
    else:
        try:
            for ii in xrange(3):
                pile1.append(s1.pop(0))
                pile2.append(s2.pop(0))
            winner = play_hand(s1, s2, pile1, pile2)
        except IndexError:
            return "PAT"
    return winner

# load cards
n1 = int(raw_input())
stack1 = []
for i in xrange(n1):
    card = raw_input()[:-1]
    stack1.append(get_card_rank(card))
n2 = int(raw_input())
stack2 = []
for i in xrange(n2):
    card = raw_input()[:-1]
    stack2.append(get_card_rank(card))

# initialize scores
n_rounds = 0
wins1 = 0
wins2 = 0
game_winner = ''

# play game
while len(stack1) > 0 and len(stack2) > 0:
    n_rounds += 1
    round_winner = play_hand(stack1, stack2)
    if round_winner == "PAT":
        game_winner = "PAT"
        break
    elif round_winner == '1':
        wins1 += 1
    else:
        wins2 += 1

# declare winner
if not game_winner:
    if wins1 > wins2:
        game_winner = '1'
    elif wins2 > wins1:
        game_winner = '2'
    else:
        game_winner = "PAT"
print game_winner, n_rounds

# test input
stack1 = [14, 13, 12]
stack2 = [13, 12, 11]