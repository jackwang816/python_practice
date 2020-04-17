def merge_sort(list_a):
    ''' Merg sort algorithm
    '''
    # copy list_a to list_b
    list_b = [x for x in list_a]
    merge_sort_split(list_b, 0, len(list_a), list_a)

def merge_sort_split(list_a, begin, end, list_b):
    '''
    Split list_a into two part and sort them respectively, 
    and then merge them in to list_b 
    '''
    # stop recursive calling when there is only one element
    if end - begin < 2:
        return
    mid = (begin + end) // 2
    # split and sort two part of list_a
    merge_sort_split(list_b, begin, mid, list_a)
    merge_sort_split(list_b, mid, end, list_a)
    # merge two part of list_a into list_b in place
    merge(list_a, begin, mid, end, list_b)

def merge(list_a, begin, mid, end, list_b):
    ''' 
    Merge two sorted part of lista into list_b
    part_one:[begin, mid)
    part_two:[mid, end)
    '''
    i, j = begin, mid
    for k in range(begin, end):
        #note: a. must add j >= end b. use <= to keep sort stable
        if i < mid and (j >= end or list_a[i] <= list_a[j]):
            list_b[k] = list_a[i]
            i += 1
        else:
            list_b[k] = list_a[j]
            j += 1

if __name__ == "__main__":
    l1 = [1,23, 5, 33, 33, 4, 12, 22]
    l2 = [2, 5, 33, 66, 4, 11, 12]
    l3 = [1]
    l4 = []
    l5 = [2, 2, 2, 2, 2, 2, 2]
    merge_sort(l1)
    print(l1)
    merge_sort(l2)
    print(l2)
    merge_sort(l3)
    print(l3)
    merge_sort(l4)
    print(l4)
    merge_sort(l5)
    print(l5)