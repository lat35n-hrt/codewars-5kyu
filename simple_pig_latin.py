import re

def piglatin_word(match):
    i = match.group()
    if len(i) == 1:
        return i[0] + 'ay'
    elif len(i) > 1:
        return i[1:] + i[0] + 'ay'

def pig_it(text):
    return re.sub(r'\b\w+\b', piglatin_word, text)




# Second
# import re
# def pig_it(text):
#     s_text = re.split(r" ", text)
#     ls = []
#     for i in s_text:
#         if len(i) == 1 and i.isalpha():
#                 ls.append(i[0] + 'ay')
#         elif len(i) > 1 and i.isalpha():
#                 ls.append(i[1:] + i[0] + 'ay')
#         else:
#             ls.append(i[0])
#     return ' '.join(ls)

# the first solution
# import re
# def pig_it(text):
#     s_text = re.split(r" ", text)
#     ls = []
#     for i in s_text:
#         if len(i) == 1:
#             if i.isalpha():
#                 ls.append(i[0] + 'ay')
#             else:
#                 ls.append(i[0])
#         elif len(i) > 1:
#             if i.isalpha():
#                 ls.append(i[1:] + i[0] + 'ay')
#     return ' '.join(ls)


# import re
# def pig_it(text):
#     s_text = re.split(r" ", text)
#     ls = []
#     for i in s_text:
#         if len(i) > 0:
#             if i.isalpha():
#                 ls.append(i[1:] + i[0] + 'ay')
#     return ' '.join(ls)





# # Test cases
# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')


# Referring other's solution
# import re
# def pig_it(text):
#     return re.sub(r'(\w{1})(\w*)', r'\2\1ay', text)