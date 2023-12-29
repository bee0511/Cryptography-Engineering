

def Berlekamp_Massey_algorithm(sequence):
    f_min = [0] # �̧C���ƪ��h����
    l = [0] # �����C���̧C�h��������
    for i in range(len(sequence)):
        d = 0
        for j in f_min: # �p��C����d
            d += sequence[i + j - max(l)]
        d = d % 2
        if d == 0: # d = 0 ��
            l.append(l[i])
        else: # d != 0 ��
            if the_same(l): # d != 0 �B l ���Ʀr�ۦP��
                n = i
                fn = f_min.copy() # copy ���D
                f_min.append(i + 1)
                l.append(i + 1)
            else: # d != 0 �B l ���Ʀr���ۦP��
                if max(f_min) > max(fn): # ���� m �M fm ����
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

def condense(f_min): # �N�h�������� mod 2
    f = list(set(f_min))
    for i in f_min:
        if f_min.count(i) % 2 == 0:
            if i in f:
                f.remove(i)
    f = sorted(f, reverse=True)
    return f
    
def the_same(l): # �P�_ l ���O�_�Ҧ��Ʀr���ۦP
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            return False
    return True

def print_f(f_min): # �٭쵲�G
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