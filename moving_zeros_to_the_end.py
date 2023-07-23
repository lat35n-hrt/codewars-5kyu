def move_zeros(lst):
    l = [i for i in lst if i != 0]
    l.extend([0] * lst.count(0))
    return l

# The second solution
# def move_zeros(lst):
#     c = lst.count(0)
#     lst = [i for i in lst if i != 0]
#     lst.extend([0] * c)
#     return lst


# The first solution
# def move_zeros(lst):
#     c = 0
#     for i in lst:
#         if i == 0:
#             c += 1

#     lst = [i for i in lst if i != 0]
    
#     while c > 0:
#         lst.append(0)
#         c -= 1
#     return lst