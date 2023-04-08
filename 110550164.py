def Berlekamp_Massey_algorithm(sequence):
    N = len(sequence) # get the length of the input sequence
    s = sequence[:] # create a copy of the sequence to work with
    for k in range(N):
        if s[k] == 1: # find the first nonzero element of the sequence
            break
    f = set([k + 1, 0])  # use a set to denote polynomial
    l = k + 1

    g = set([0]) # initialize a temporary variable to store old versions of f
    a = k
    b = 0

    for n in range(k + 1, N):  # loop over the remaining elements of the sequence
        d = 0
        for ele in f:
            d ^= s[ele + n - l] # compute the discrepancy between the LFSR output and the sequence

        if d == 0:
            b += 1
        else:
            if 2 * l > n: # if the LFSR is short enough, update f using g
                f ^= set([a - b + ele for ele in g])
                b += 1
            else: # if the LFSR is too long, update f and g
                temp = f.copy()
                f = set([b - a + ele for ele in f]) ^ g
                l = n + 1 - l
                g = temp
                a = b
                b = n + 1 - l

    # output the polynomial
    def print_poly(polynomial):
        result = ''
        lis = sorted(polynomial, reverse=True)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '

        return result

    return (print_poly(f), l) # return the LFSR polynomial and its length

if __name__ == '__main__':
    # seq = ( 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1)
    # seq = (0, 0, 0, 1, 0, 0, 1, 1) 
    seq = (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)
    (poly, span) = Berlekamp_Massey_algorithm(seq)

    print ('The input sequence is', seq)
    print ('Its characteristic polynomial is', poly)
    print ('and linear span is', span)