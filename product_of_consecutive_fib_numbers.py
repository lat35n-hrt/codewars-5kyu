#Recursion
def productFib(prod, a=0, b=1):
    if a * b == prod:
        return [a, b, True]
    elif a * b > prod:
        return [a, b, False]
    else:
        return productFib(prod, b, a + b)



# Submitted once
# def productFib(prod):
#     f = [0, 1]
#     for n in range(prod+1):
#         x = f[n] + f[n+1]
#         y = f[n] * f[n+1]
#         if y < prod:
#             f.append(x)
#         elif y == prod:
#             return [f[n], f[n+1], True]
#         else:
#             return [f[n], f[n+1], False]





# FAILED
# def productFib(prod):
#     f = [0, 1]
#     for n in range (prod):
#         x = f[n] + f[n+1]
#         y = f[n] * f[n+1]
#         if y < prod:
#             f.append(x)
#         elif y == prod:
#             return [f[n], f[n+1], True]
#         else:
#             return [f[n], f[n+1], False]

# Failed at attemopt prod = 0 to 3
# None should equal [0, 1, True] 
# None should equal [1, 1, True]
# None should equal [1, 2, True]
# None should equal [2, 3, False]




# The third solution
# def productFib(prod):
#     f = [0, 1]
#     for n in range (prod):
#         x = f[n] + f[n+1]
#         if f[n] * f[n+1] < prod:
#             f.append(x)
#         elif f[n] * f[n+1] == prod:
#             return [f[n], f[n+1], True]
#         else:
#             return  [f[n], f[n+1], False]

# The second solution
# def productFib(prod):
#     fib = [0, 1]
#     # n = 0 
#     next = 0
#     for n in range (prod):
#         next = fib[n] + fib[n+1]
#         if fib[n] * fib[n+1] < prod:
#             fib.append(next)
#             # n += 1
#         elif fib[n] * fib[n+1] == prod:
#             return [fib[n], fib[n+1], True]
#         else:
#             return  [fib[n], fib[n+1], False]


# The first solution
# def productFib(prod):
#     fib_list = [0, 1]
#     n = 0 
#     next_value = 0
#     for item in range (prod):
#         next_value = fib_list[n] + fib_list[n+1]
        
#         print(fib_list[n])
#         print(fib_list[n+1])
#         print(next_value)
#         print("---")
        
#         if fib_list[n] * fib_list[n+1] == prod:
#             return [fib_list[n], fib_list[n+1], True]
#         elif fib_list[n] * fib_list[n+1] < prod:
#             fib_list.append(next_value)
#             n += 1
#         else:
#             return  [fib_list[n], fib_list[n+1], False]
        
 




#[After submit research]
# Referred @Frostmilk-Dragon
# def productFib(prod):
#     # your code
#     F = [0, 1]
#     n = 0
#     while True:
#         if F[n]*F[n+1] >= prod:
#             return [F[n] , F[n+1] , F[n]*F[n+1] == prod]
#         F.append(F[n] + F[n+1])
#         n += 1


