# set example (also fit frozenset)
set_org = {'jwwang', 'head', 'curl'}
assert(len(set_org) == 3)
assert('jwwang' in set_org)
assert('jwwang_1' not in set_org)
set_disjoint = {'amazon', 'goole', 'set'}
set_sub = {'jwwang', 'head'}
assert(set_org.isdisjoint(set_disjoint))
assert(not set_org.isdisjoint(set_sub))
assert(set_sub.issubset(set_org))
assert(set_org.issuperset(set_sub))
assert(set_sub <= set_org)
assert(set_org >= set_sub)
assert(set_sub < set_org)
set_union = set_org | set_disjoint | set_sub
set_union = set_org.union(set_disjoint, set_sub)
print set_union # 'jwwang', 'set', 'curl', 'head', 'amazon', 'goole'
set_inter = set_org.intersection(set_sub)
print set_inter # 'head', 'jwwang'
set_inter = set_org & set_disjoint
print set_inter # {}
set_diff = set_org.difference(set_disjoint)
print set_diff # 'jwwang', 'head', 'curl'
set_diff = set_org - set_sub
print set_diff # 'curl'
set_symdiff = set_org.symmetric_difference(set_disjoint)
print set_symdiff # 'jwwang', 'set', 'head', 'goole', 'amazon', 'curl'
set_new = {'jwwang', 'head', 'abc'}
set_symdiff = set_org ^ set_new
print set_symdiff # 'abc', 'curl'
# shallow copy
set_cpy = set_org.copy()

# set example (not fit frozenset which is immutable)
set_org = {'jwwang', 'head', 'curl'}
set_add = {'add1'}
set_org.update(set_add)
print set_org # 'jwwang', 'curl', 'head', 'add1'
set_org |= set_add
print set_org # 'jwwang', 'curl', 'head', 'add1'
# same as set_org &= set_add & ...
set_org.intersection_update(set_add) 
print set_org # 'add1'
# difference_update(*others)(set-= other | ...)
# symmetric_difference_update(other) (set ^= other)
set_org.add('jwwang')
set_org.remove('add1')
print set_org # 'jwwang'
# set_org.remove('add1') will raise KeyError since 'add1' no loger in set
set_org.discard('add1') # won't raise KeyError
set_org.clear()
# set_org.pop() will raise KeyError since set_org has been clear