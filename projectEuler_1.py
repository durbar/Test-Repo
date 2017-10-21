"""
One of the most elegant solution to project Eular's first question: get the sum of multiples of 3 and 5 between 0 and the given input integer

sample Input:
1
10

Output
23
"""

n = lambda s : s*(s+1)/2
t = lambda r : n(r/3)*3 +n(r/5)*5 - n(r/15)*15
print '\n'.join(str(t(int(raw_input()) - 1)) for x in xrange(int(raw_input())))

