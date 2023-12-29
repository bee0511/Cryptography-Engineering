

def Berlekamp_Massey_algorithm(sequence):
    f_min = [0] # 程Ω计兜Α
    l = [0] # 魁–Ω程兜ΑΩ计
    for i in range(len(sequence)):
        d = 0
        for j in f_min: # 璸衡–Ωd
            d += sequence[i + j - max(l)]
        d = d % 2
        if d == 0: # d = 0 
            l.append(l[i])
        else: # d != 0 
            if the_same(l): # d != 0  l い计
                n = i
                fn = f_min.copy() # copy 拜肈
                f_min.append(i + 1)
                l.append(i + 1)
            else: # d != 0  l い计ぃ
                if max(f_min) > max(fn): # 魁 m ㎝ fm 
                    m = n
                    fm = fn.copy()
                n = i
                fn = f_min.copy()
                if m - l[m] >= n - l[n]:
                    f_min += [j + (m - l[m] - n + l[n]) for j in fm] 
                else: 
                    f_min = [j - (m - l[m] - n + l[n]) for j in f_min] + fm
                l.append(max(f_min))
    f_min = condense(f_min)
    return f_min

def condense(f_min): # 盢兜Α场 mod 2
    f = list(set(f_min))
    for i in f_min:
        if f_min.count(i) % 2 == 0:
            if i in f:
                f.remove(i)
    f = sorted(f, reverse=True)
    return f
    
def the_same(l): # 耞 l い琌┮Τ计常
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            return False
    return True

def print_f(f_min): # 临挡狦
    result = ''
    for i in f_min:
        if i == 0:
            result += '1'
        else:
            result += 'x^' + str(i)
        if i != f_min[-1]:
            result += '+'
    return result
    
if __name__ == '__main__':
    
    seq = ( 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1)
    # seq = (0, 0, 0, 1, 0, 0, 1, 1) 
    # seq = [1, 0, 1, 1, 0, 0, 0, 1]
    poly = Berlekamp_Massey_algorithm(seq)
    print ('The input sequence is', seq)
    print ('Its characteristic polynomial is', print_f(poly))
    print ('and linear span is', str(max(poly)))