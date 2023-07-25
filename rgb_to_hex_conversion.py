def value_to_hex(y):
    if y < 0: y = 0
    elif y > 255: y = 255
    return hex(y)[2:].zfill(2).upper()

def rgb(r, g, b):
    return ''.join(value_to_hex(c) for c in (r, g, b))


# The fourth solution
# def value_to_hex(y):
#     if y < 0: y = 0
#     elif y > 255: y = 255
#     return hex(y)[2:].zfill(2).upper()

# def rgb(r, g, b):
#     return value_to_hex(r)+value_to_hex(g)+value_to_hex(b)





# The third solution
# def conversion(y):
#     if 0 <= y <=255:
#         h_y = hex(y)[2:]
#     elif y < 0:
#         h_y = '00'
#     elif y > 255:
#         h_y = 'FF'
#     return h_y.zfill(2).upper()

# def rgb(r, g, b):
#     return conversion(r)+conversion(g)+conversion(b)



# The second solution
# def conversion(y):
#     if (0 <= y <=255) and len(hex(y)) == 3:
#         h_y = hex(y).replace('x', '')
#     elif (0 <= y <=255) and len(hex(y)) == 4:
#          h_y = hex(y).replace('0x', '')
#     elif y < 0:
#         h_y = '00'
#     elif y > 255:
#         h_y = 'FF'
#     return h_y.upper()

# def rgb(r, g, b):
#     return conversion(r)+conversion(g)+conversion(b)

# The first solution
# def rgb(r, g, b):
#     if len(hex(r))==3 and (0 <= r <=255):
#         h_r = hex(r).replace('x', '')
#     elif len(hex(r))==4 and (0 <= r <=255):
#          h_r = hex(r).replace('0x', '')
#     elif r < 0:
#         h_r = '00'
#     elif r > 255:
#         h_r = 'FF'

#     if len(hex(g))==3 and (0 <= g <=255):
#         h_g = hex(g).replace('x', '')
#     elif len(hex(g))==4 and (0 <= g <=255):
#          h_g = hex(g).replace('0x', '')
#     elif g < 0:
#         h_g = '00'
#     elif g > 255:
#         h_g = 'FF'
    
#     if len(hex(b))==3 and (0 <= b <=255):
#         h_b = hex(b).replace('x', '')
#     elif len(hex(b))==4 and (0 <= b <=255):
#         h_b = hex(b).replace('0x', '')
#     elif b < 0:
#         h_b = '00'
#     elif b > 255:
#         h_b = 'FF'
    
#     return str(h_r).upper()+str(h_g).upper()+str(h_b).upper()



# Decimal(10): 0-155
# Hex (16)

# Description
# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

# [Test cases]
# test.assert_equals(rgb(0, 0, 0), "000000", "testing zero values")
# test.assert_equals(rgb(1, 2, 3), "010203", "testing near zero values")
# test.assert_equals(rgb(255, 255, 255), "FFFFFF", "testing max values")
# test.assert_equals(rgb(254, 253, 252), "FEFDFC", "testing near max values")
# test.assert_equals(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


# Hex() only
# testing zero values: '0x00x00x0' should equal '000000'
# testing near zero values: '0x10x20x3' should equal '010203'
# testing max values: '0xff0xff0xff' should equal 'FFFFFF'
# testing near max values: '0xfe0xfd0xfc' should equal 'FEFDFC'
# testing out of range values: '-0x140x1130x7d' should equal '00FF7D'


'-0x140 x113 0x7d'


#[after submit research]
# def rgb(r, g, b):
    # return ''.join([hex((max(min(255, n), 0)))[2:].upper().zfill(2) for n in (r, g, b)])