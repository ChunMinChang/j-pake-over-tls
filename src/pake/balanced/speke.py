#   Utils
# =======================================
# printTable
# ----------------
# @table
#   [ (1-1, 1-2, ..., 1-m),
#     (2-1, 2-2, ..., 2-m),
#     ..
#     (n-1, n-2, ..., n-m),
#   ]
def printTable(table):
    # zipped = [
    #   (1-1, 2-1, ..., n-1),
    #   (1-2, 2-2, ..., n-2),
    #   ....
    #   (1-m, 2-m, ..., n-m)]
    zipped = zip(*table)
    # colWidth = [maxLen(i-1), maxLen(i-2), ..., maxLen(i-m)], where i = 1 ~ n
    colWidth = [max(len(ele) for ele in col) for col in zipped]
    for row in table: # row = (i-1, i-2, ..., i-m), where i = 1 ~ n
        print '| ' + ' | '.join('{:{}}'.format(val, colWidth[idx]) for idx, val
                in enumerate(row)) + ' |'
        # enumerate(row) = [(0, i-1), (1, i-2), (2, i-3), ...(m-1, i-m)]
        # idx = 0, 1, 2, ... m-1
        # val = i-1, i-2, i-3, ...., i-m
        # idx = k - 1, where k = 1 ~ m
        #   val = i-k
        #   colWidth[idx] = maxLen(i-k)

        # When m = 3, the above statment will be same as the following:
        # print '| {0:<{col0}} | {1:<{col1}} | {2:<{col2}} |'.format(row[0],
        #     row[1], row[2], col0=colWidth[0], col1=colWidth[1], col2=colWidth[2])

#   SPEKE
# =======================================
q = 11          # a prime number to produce a safe prime
p = 2*q + 1     # Modulo p for multiplicative group of integers
G = range(1, p) # Group G = { 1, 2, 3, ..., p-1 }

# f
# ----------------
# a function to produce the generator g
# @x
#   any integer
# Returns a generator for a cyclic subgroup of G
def f(x): # f(x) = x^2 mod p
    return pow(x, 2, p)

# generateGroup
# ----------------
# @g
#   any value produced from f(x)
# Returns a cyclic subgroup of G
def generateCyclicGroup(g):
    group = []
    power = 0
    while True:
        power = power + 1
        element = pow(g, power, p)
        if power != 1 and element == g:
            break;
        else:
            group.append(element)
    return group


#   Main program
# =======================================
# getPairs
# ----------------
# returns a table like:
#   [ (password, generator, subgroup, sorted subgroup),
#     ('1', '1', '1', '1'),
#     ('2', '4', '4, 16, 18, 3, 12, 2, 8, 9, 13, 6, 1', '1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18'),
#     ('3', '9', '9, 12, 16, 6, 8, 3, 4, 13, 2, 18, 1', '1, 2, 3, 4, 6, 8, 9, 12, 13, 16, 18'),
#     ...
#     ... ]
def getPairs():
    # pair = [(x, f(x), generateCyclicGroup(f(x))) for x in G]
    pair = []
    for x in G:
        generator = f(x)
        subgroup = generateCyclicGroup(generator)
        sortedSubgroup = sorted(subgroup)
        # subgroup.sort()
        # pair.append((str(x), str(generator), ', '.join(str(e) for e in subgroup)))
        pair.append((str(x), str(generator), str(subgroup)[1:-1], str(sortedSubgroup)[1:-1]))

    table = [('password', 'generator', 'subgroup', 'sorted subgroup')] + pair
    return table

# Show the password-generator-subgroup pairs
printTable(getPairs())
