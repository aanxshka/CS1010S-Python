def merge_lists(all_lst):
    final_lst = []
    for lst in all_lst:
        for i in lst:
            final_lst.append(i)
    
    def sort(lst):
        sort = []
        while final_lst:
            smallest = 9999
            for j in final_lst:
                if j < smallest:
                    smallest = j
            final_lst.remove(smallest)
            sort.append(smallest)
        return sort
        
    return sort(final_lst)

def merge(lists, field):
    final_lst = []
    for lst in lists:
        for i in lst:
            final_lst.append(i)
    sort = []
    while final_lst:
        smallest = ["CS9999", "ZZZZ", "ZZZZ"]
        for module in final_lst:
            if field(module) < field(smallest):
                smallest = module
        final_lst.remove(smallest)
        sort.append(smallest)
        
    return sort



