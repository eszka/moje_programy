__author__ = 'Agnieszka'

my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

lambda x: x % 3 == 0

Is the same as:
def by_three(x):
    return x % 3 == 0
