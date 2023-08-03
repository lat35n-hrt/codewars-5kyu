# The second solution
def rot13(message):
    return ''.join(chr(ord('a') + (ord(i)-ord('a')+13) % 26) if 'a' <= i <= 'z' else 
                   chr(ord('A') + (ord(i)-ord('A')+13) % 26) if 'A' <= i <= 'Z' else 
                   chr(ord(i)) for i in message)

# The first solution
# def rot13(message):
#     c=[]
#     for i in message:
#         if 'a' <= i <= 'z':
#             pos = ord('a') + (ord(i)-ord('a')+13) % 26
#         elif 'A' <= i <= 'Z':
#             pos = ord('A') + (ord(i)-ord('A')+13) % 26
#         else:
#             pos = ord(i)
#         c.append(chr(pos))
#     return ''.join(c)







# from solution import rot13

# @test.describe("Fixed tests")
# def tests():
        
#     @test.it("Should obtain correct Rot13 encoding on fixed strings")
#     def test_rot13_fixed_strings():
#         test.assert_equals(rot13('test'), 'grfg', 'Returned solution incorrect for fixed string = test')
#         test.assert_equals(rot13('Test'), 'Grfg', 'Returned solution incorrect for fixed string = Test')
#         test.assert_equals(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%', 'Returned solution incorrect for fixed string = aA bB zZ 1234 *!?%')