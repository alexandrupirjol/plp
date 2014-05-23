import sys, os

def qsort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x.keys()[0] < pivot.keys()[0]:
                less.append(x)
            if x.keys()[0] == pivot.keys()[0]:
                x_value = x.values()[0].get('value')
                pivot_value = pivot.values()[0].get('value')
                if x_value < pivot_value:
                    less.append(x)
                if x_value == pivot_value:
                    equal.append(x)
                if x_value > pivot_value:
                    greater.append(x)
            if x.keys()[0] > pivot.keys()[0]:
                greater.append(x)
        return qsort(less)+equal+qsort(greater)
    else:
        return array

def parse_input(fs):
    ls = []
    if os.path.exists(fs):
        with open(fs, 'r') as f:
            ls =[{x.split(" ")[0]: {'value': x.split(" ")[1],
                                    'index': i}}
                for i, x in enumerate(f.read().splitlines())]
            f.close()
    return ls

def format_output(ls, out):
    with open(out, 'w') as f:
        for i in ls:
            f.write(str(i.values()[0].get('index'))+"\n")
        f.close()

def sort_list(fs=None, out=None):
    # No command line arguments or bad arguments, set defaults
    if not fs or not os.path.exists(fs):
        fs = 'plp_phase1_p3_in.txt'
    if not out:
        out = 'plp_phase1_p3_out.txt'

    ls = parse_input(fs)
    sorted_ls = qsort(ls)
    format_output(sorted_ls, out)

if __name__ == "__main__":
    try:
        input_file = sys.argv[1] if len(sys.argv) >= 2 else None
        output_file = sys.argv[2] if len(sys.argv) >= 3 else None
        sort_list(input_file, output_file)
    except (NameError, ValueError) as e:
        print "ERROR :: Invalid arguments :: {0}".format(e)
