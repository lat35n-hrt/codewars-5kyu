# The second solution
def generate_hashtag(s):
    if s is '' or len(s) > 140 : return False
    return '#' + ''.join(i.capitalize() for i in s.split())


# The first solution
# def generate_hashtag(s):
#     c = []
#     if s is '' or len(s) > 140 :
#         return False
#     for i in s.split():
#         c.append(i.capitalize())
#     return '#'+ ''.join(c)



# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false