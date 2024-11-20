lst = [156, 90, 1, 2, 5, 3, 9, 0, 7]

def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    
    else:
        pivot = lst[len(lst) // 2]
        left = [x for x in lst if x < pivot]
        right = [x for x in lst if x > pivot]
        return quick_sort(left) + [pivot] + quick_sort(right)

sortlst = quick_sort(lst)
print(sortlst)