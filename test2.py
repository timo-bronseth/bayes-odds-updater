# my_list = [1, 2, 3, 4, 5]
# my_list = iter(my_list)
#
# while i := next(my_list):
#     print(i)

my_list = range(100)


def my_generator(n=0):
    while i := 0 < n:
        yield i
        i += 1


my_set = [x*2 for x in range(9999) if x**2 > 3]

print(my_set)