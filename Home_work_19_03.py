##### 19/03/2023 ######
# 1)
# def print_skipped(list):
#     for m in range(0, len(list), 2):
#         print(list[m])
#
# print_skipped([8, 11, 'bla', True, 2])

# 2)
# def tuple_received(t):
#     l = []
#     for elem in t:
#         if elem not in l:
#             l.append(elem)
#     return tuple(l)
# x = tuple_received([5, 5, 9, 7, 8, 9])
# print(x)

#  3)
# def match_name(first_name, last_name):
#     d = {}
#
#     for first in first_name:
#         for last in last_name:
#             if first[0] == last[0]:
#                 d[first] = last
#     return d
#
# print(match_name(['Sue', 'Peter', 'Matt', 'Bruce'], ['Parker', 'Banner', 'Storm', 'Murdock']))
