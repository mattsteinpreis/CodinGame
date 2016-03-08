__author__ = 'matt'


def load_system(s, w, h):
    """
    Load the ascii and numerical represenations of the system.
    :param s: the full string consisting of 20 visual representations.
    :param w: width of one character
    :param h: height (# of line) of one character
    The first 20*L characters will be the top lines of all 20 characters, the second
    20*L characters the second lines, and so on.
    :return: a dict containing all visual to numeric and numeric to visual relations.
    """
    d = {}
    skip = w*20
    for ii in xrange(20):
        start = ii*w
        si = ''
        for jj in xrange(h):
            si = si + s[(start+skip*jj):(start+skip*jj+w)]
        d[si] = ii
        d[ii] = si
    return d


def decode_number(t, h, h_dig, w_dig, num_dict):
    total_sum = 0
    ndigits = h / h_dig
    l_dig = h_dig * w_dig
    for ii in xrange(ndigits):
        factor = 20**(ndigits-ii-1)
        vis_rep = t[(ii*l_dig):((ii+1)*l_dig)]
        dig_rep = num_dict[vis_rep]
        total_sum += dig_rep*factor
    return total_sum


def encode_number(n, h, w, num_dict):
    # get base 20 digits
    base20_digits = []
    max_exp = 0
    while n > 20**(max_exp+1):
        max_exp += 1
    for ii in xrange(max_exp+1):
        factor = 20**(max_exp - ii)
        base20_digits.append(n / factor)
        n = n % factor

    # get visual reps of digits
    l = []
    for digit in base20_digits:
        s = num_dict[digit]
        for ii in xrange(h):
            l.append(s[ii*w:(ii+1)*w])
    return l


def perform_operation(n1, n2, op):
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2
    if op == '*':
        return n1*n2
    return n1 / n2


# load parameters
width, nlines_digit = [int(i) for i in raw_input().split()]
# load system
mayan_rep = ''
for i in xrange(nlines_digit):
    mayan_rep = mayan_rep + raw_input()
num_system = load_system(mayan_rep, width, nlines_digit)

# get numbers
term1 = ''
size1 = int(raw_input())
for i in xrange(size1):
    term1 = term1 + raw_input()
term2 = ''
size2 = int(raw_input())
for i in xrange(size2):
    term2 = term2 + raw_input()
operation = raw_input()

num1 = decode_number(term1, size1, nlines_digit, width, num_system)
num2 = decode_number(term2, size2, nlines_digit, width, num_system)
dig_result = perform_operation(num1, num2, operation)
viz_result_list = encode_number(dig_result, nlines_digit, width, num_system)
for line in viz_result_list:
    print line


# test parameters
width, nlines_digit = [4, 4]
mayan_rep = ('.oo.o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo....o...oo..ooo.oooo' +
             'o..o................____________________________________________________________' +
             '.oo.....................................________________________________________' +
             '............................................................____________________')
size1 = 4
term1 = 'ooo.____________'
size2 = 4
term2 = 'ooo.............'
operation = '+'

# test 2
width, nlines_digit = [1, 1]
mayan_rep = '0123456789ABCDEFGHIJ'