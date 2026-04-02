def add_binary(a, b):
    o_a = a[2:]
    a_1 = 0
    o_e = b[2:]
    b_1 = 0
    
    for i in range(len(a) - 2):
        a_1 += (2 ** (len(o_a) - 1 - i)) * int(o_a[i])
    for j in range(len(b) - 2):
        b_1 += (2 ** (len(o_e) - 1 - j)) * int(o_e[j])
         
        
    c_1 = a_1 + b_1
    res = bin(c_1)
    return res 
    '''
    Given two strings perform binary addition and return the result as a string
    '''