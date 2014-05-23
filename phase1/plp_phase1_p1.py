import sys

def flatten(list_a, list_b, max_depth):

    def is_iterable(ls):
        return hasattr(ls, '__iter__') and not isinstance(ls, dict)

    def add_items(l_1, l_2):
        if not is_iterable(l_1):
            l_1 = [l_1]
        if not is_iterable(l_2):
            l_2 = [l_2]
        return list(l_1) + list(l_2)

    def flatten_list(l, m_depth, c_depth=-1):
        is_flat = True
        for i in l:
            if is_iterable(i):
                is_flat = False
        c_depth += 1
        if(c_depth < m_depth and not is_flat):
            return flatten_list(reduce(add_items, l), m_depth, c_depth)
        return l

    print flatten_list(list_a, max_depth), flatten_list(list_b, max_depth)
    return flatten_list(list_a, max_depth), flatten_list(list_b, max_depth)

if __name__ == "__main__":
    try:
        flatten(eval(sys.argv[1]), eval(sys.argv[2]), int(sys.argv[3]))
    except (NameError, ValueError) as e:
        print "ERROR :: Invalid arguments :: {0}".format(e)
