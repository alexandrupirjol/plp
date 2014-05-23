import sys

def merge(obj_a, obj_b):

    def add_items(first_item, second_item):
        try:
            return first_item + second_item
        except:
            try:
                return first_item.union(second_item)
            except:
                try:
                    return first_item.update(second_item)
                except:
                    return (first_item, second_item)

    def merge_dicts(first, second):
        for k, v in first.iteritems():
            if k in second.keys():
                if not isinstance(v, dict) and not isinstance(second[k], dict):
                    first[k] = add_items(v, second[k])
                else:
                    first[k] = merge_dicts(v, second[k])
                del second[k]

        first.update(second)
        return first

    result = merge_dicts(obj_a, obj_b)
    print result
    return result

if __name__ == "__main__":
    try:
        merge(eval(sys.argv[1]), eval(sys.argv[2]))
    except (NameError, ValueError) as e:
        print "ERROR :: Invalid arguments :: {0}".format(e)
