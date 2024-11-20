class Sort_list_even_reversodd:

    def __init__(self, lst):
        self.lst = lst
        self.even = []
        self.odd = []

    def even_odd(self):
        for digit in self.lst:
            if digit % 2 == 0:
                self.even.append(digit)
            else:
                self.odd.append(digit)
        return self.even, self.odd
    
    def quick_sort(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            pivot = lst[len(lst) // 2]
            left = [x for x in lst if x < pivot]
            middle = [x for x in lst if x == pivot]
            right = [x for x in lst if x > pivot]
            return self.quick_sort(left) + middle + self.quick_sort(right)

    def sort_even_odd(self):
        even_lst, odd_lst = self.even_odd()
        sorted_even = self.quick_sort(even_lst)
        sorted_odd = sorted(self.quick_sort(odd_lst), reverse = True)
        return sorted_even + sorted_odd

lst = [10, 3, 2, 7, 6, 8, 1, 5]
sorter = Sort_list_even_reversodd(lst)

result = sorter.sort_even_odd()
print(result)