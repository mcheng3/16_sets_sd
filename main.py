A = [1, 2, 3]
B = [2, 3, 4]
print 'A: ' + str(A)
print 'B: ' + str(B) + '\n'

def union(n, m):
    return [i for i in n if i not in m] + m
print 'A U B: ' + str(union(A, B)
)
def intersection(n, m):
    return [i for i in n if i in m]
print 'intersection : ' + str(intersection(A, B))

def set_diff(n, m):
    return [i for i in n if i not in m]
print 'A/B: ' + str(set_diff(A, B))

def sym_diff(n, m):
    return set_diff(union(n, m), intersection(n, m))
print 'symmetric difference: ' + str(sym_diff(A, B))

def cartesian_prod(n, m):
    return [[i, j] for i in n for j in m]
print 'A x B: ' + str(cartesian_prod(A, B))