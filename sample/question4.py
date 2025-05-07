# Write a function called print_list_indexes() that takes 2 parameters:
# String
# an arbitrarily complex nested list
# The function should print the value of each list element on a separate line. The value of each line should be preceded by the string and numbers indicating the depth and index of the element in the list. Assume that the list contains only strings and other nested lists.
# Input:
# my_list = ['h', 'a', ['e','b'], 'c']
# arb_str = 'Foo'
# Output:
# Foo:0 h
# Foo:1 a
# Foo.2:0 e
# Foo.2:1 b
# Foo:3 c
def iterate(arb_str, nested_list, layer=0, index_str=''):
    for index, value in enumerate(nested_list):
        if isinstance(value, list):
            layer += 1
            index_str += str(index) + ':'
            iterate(arb_str, value, layer, index_str)
        else:
            if layer == 0:
                print(arb_str + ':' + str(index) + ' ' + value)
            else:
                print(arb_str + '.' + index_str + str(index) + ' ' + value)

my_list = ['h', 'a', ['e','b', ['oaoisd', 'laksjl', 'lkx']], 'c']
arb_str = 'Foo'
iterate(arb_str, my_list)