# The third solution
import math
def decomp(n):
    fn = math.factorial(n)
    ls = []
    a = []
    for i in range(2, n+1):
        for p in range(2, i):
            if i % p != 0:
                continue
            elif p == (i-1):
                ls.append(i)
                break
    for t in ls:
        k = 0
        while fn >= t:
            if fn % t == 0:
                fn //= t
                k += 1
            else:
                break
        if k == 1:
            a.append(str(t))
        elif k > 1:              
            a.append(f"{t}^{k}")
    return ' * '.join(a)


# The second solution
# import math

# def decomp(n):
#     fn = math.factorial(n)
#     ls = []
#     answer = []
#     for i in range(2, n+1):
#         ls.append(i)
#         for p in range(2, i):
#             if i % p == 0:
#                 ls.remove(i)  
#                 break
    
#     for t in ls:
#         k = 0
#         while fn >= t:
#             if fn % t == 0:
#                 fn //= t
#                 k += 1
#             else:
#                 break     

#         if k == 0:
#             pass
#         elif k == 1:
#             answer.append(str(t))
#         else:              
#             answer.append(str(t)+'^'+str(k))

#     return ' * '.join(answer)


# The first solution
# import math

# def decomp(n):
#     fn = math.factorial(n)
#     ls = []
#     answer = []
#     for i in range(2, n+1):
#         ls.append(i)
#         for p in range(2, i):
#             if i % p == 0:
#                 ls.remove(i)  
#                 break
#     print(ls)
    
#     for t in ls:
#         k = 0
#         while fn >= t:
#             if fn % t == 0:
#                 k += 1
#                 fn //= t
#             else:
#                 break     
#         if k == 1:
#             answer.append(str(t))
#         elif k == 0:
#             answer.append('')
#         else:              
#             answer.append(str(t)+'^'+str(k))


#     return ' * '.join(answer)


### TIMEOUT ####
### TRY AGAIN ####

# import math
# def decomp(n):
#     answer = []
#     f_n = math.factorial(n)
#     for i in range(2, f_n):
#         count = 0
#         while f_n % i == 0:
#             count += 1
#             f_n = f_n // i
#         if n >= 2:
#             answer.append(str(i)+'^'+str(count))
#         elif n == 1:
#             answer.append(str(i))
#     return ' * '.join(answer)

    # Test
    # test.assert_equals(decomp(5), "2^3 * 3 * 5")
    # test.assert_equals(decomp(14), "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13")