import numpy as np
import galois
def Berlekamp_Massey_algorithm(sequence):
    N = len(sequence) # get the length of the input sequence
    a = galois.Poly((np.flip(np.array([0] * N + [1]))), field=GF)
    b = galois.Poly(np.array(sequence), field=GF)
    x, prevx = galois.Poly(np.array([0]), field=GF), galois.Poly(np.array([1]), field=GF)
    y, prevy = galois.Poly(np.array([1]), field=GF), galois.Poly(np.array([0]), field=GF)
    while(len(prevy) < len(b)):
        q, r = a // b, a % b
        a, b = b, r
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
    return prevy, prevy.nonzero_degrees[0]
    
if __name__ == '__main__':
    
    GF = galois.GF2
    seq = ( 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1)
    # seq = (0, 0, 0, 1, 0, 0, 1, 1) 
    # seq = [1, 0, 1, 1, 0, 0, 0, 1]
    (poly, span) = Berlekamp_Massey_algorithm(seq)

    print ('The input sequence is', seq)
    print ('Its characteristic polynomial is', poly)
    print ('and linear span is', span)