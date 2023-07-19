# Submitted solution 

import itertools
def choose_best_sum(t, k, ls):
    if not (t >= 0 and k >= 1):
        return None

    s = map(sum,itertools.combinations(ls, k))
    v = list(filter(lambda x: x <= t, s))

    return max(v) if v else None





# The forth
# import itertools
# def choose_best_sum(t, k, ls):
#     a= []
#     if not (t >= 0 and k >= 1):
#         return None

#     for c in itertools.combinations(ls, k):
#         s = sum(c)
#         if s <= t:
#             a.append(s)
    
#     return max(a) if a else None










## The third solution
# import itertools
# def choose_best_sum(t, k, ls):
#     l = []
#     if not (t >= 0 and k >= 1):
#         return None

#     for item in itertools.combinations(ls, k):
#         if sum(item) <= t:
#             l.append(sum(item))
    
#     return max(l) if l else None


## The second solution
# import itertools
# def choose_best_sum(t, k, ls):
#     combination = itertools.combinations(ls, k)
#     answer = []
#     if not (t >= 0 and k >= 1):
#         return None
#     else:
#         for item in combination:
#             if sum(item) <= t:
#                 answer.append(sum(item))
#         if len(answer)==0:
#             return None
#     return max(answer)






# The first solution
# import itertools

# def choose_best_sum(t, k, ls):
#     if not (t >= 0 and k >= 1) or k > len(ls):
#         return None

#     answer=0
#     for item in itertools.combinations(ls, k):
#         if sum(item) <= t:                
#             if answer < sum(item):
#                 answer = sum(item)
#     if answer == 0:
#         return None
#     else:
#         return answer





 # t: max sum of distance
 # k: number of town to visit