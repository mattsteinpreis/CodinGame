__author__ = 'matt'


def quick_finish(t, i, n, history):
    amt_repeated = t
    n_repeats = n / (i+1)
    total_repeated = n_repeats * amt_repeated
    remaining = n - (n_repeats * (i+1))
    if remaining > 0:
        total_repeated += history[remaining - 1]
    return total_repeated


# get inputs
n_seats, n_rides, n_groups = [int(i) for i in raw_input().split()]
groups = []
total_riders = 0
for i_group in xrange(n_groups):
    group_i = int(raw_input())
    groups.append(group_i)
    total_riders += group_i

cumul_ride_history = {}
total_money = 0
group_i = 0
first_groups = [0]*n_groups
for i_ride in xrange(n_rides):
    on_board = 0
    first_group[group_i] += 1
    while on_board + groups[group_i] <= n_seats:
        g = groups[group_i]
        on_board += g
        group_i += 1
        if group_i == n_groups:
            group_i = 0
        if on_board == total_riders:
            break
    total_money += on_board
    cumul_ride_history[i_ride] = total_money
    if group_i == 0:
        total_money = quick_finish(total_money, i_ride, n_rides, cumul_ride_history)
        break

print total_money