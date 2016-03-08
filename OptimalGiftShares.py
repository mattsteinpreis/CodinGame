__author__ = 'matt'

# For "The Gift"


def optimal_shares(cost, budgets):
    total = sum(budgets)
    l = len(budgets)
    if total < cost:
        return ["IMPOSSIBLE"]
    bsorted = sorted(budgets)
    shares = []
    for budget in bsorted:
        avg = cost/l
        share = min(budget, avg)
        shares.append(share)
        cost -= share
        l -= 1
    return shares


n = int(raw_input())
my_cost = int(raw_input())

my_budgets = []
for i in xrange(n):
    my_budgets.append(int(raw_input()))

my_payments = optimal_shares(my_cost, my_budgets)

for payment in my_payments:
    print payment
