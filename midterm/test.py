import binascii

message = "The"

def ascii_to_hex(s):
    tmp = ""
    for ch in s:
        tmp += format(ord(ch), "x")
    return tmp
print(ascii_to_hex(message))

key = "66396e89c9dbd8cc9874352acd6395102eafce78aa7fed28a07f6bc98d29c50b69b0339a19f8aa401a9c6d708f80c066c763fef0123148cdd8e802d05ba98777335daefcecd59c433a6b268b60bf4ef03c9a611098bb3e9a3161edc7b804a33522cfd202d2c68c57376edba8c2ca50027c61246ce2a12b0c4502175010c0a1ba4625786d911100797d8a47e98b0204c4ef06c867a950f11ac989dea88fd1dbf16748749ed4c6f45b384c9d96c4"
text = "32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"


def hex_to_binary(num):

    scale = 16 ## equals to hexadecimal

    num_of_bits = 4

    
    return bin(int(num, scale))[2:].zfill(num_of_bits)

def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1
     
    # counter to check group of 4
    count = 1
     
    # char array to store hexadecimal number
    hexaDeciNum = ['0'] * 100
     
    # counter for hexadecimal number array
    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)
         
        # check if group of 4 completed
        if count % 4 == 0:
           
            # check if temp < 10
            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
             
        # group of 4 is not completed
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
         
    # check if at end the group of 4 is not
    # completed
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
         
    # check at end the group of 4 is completed
    if count == 1:
        i = i-1
         
    # printing hexadecimal number
    # array in reverse order
    return hexaDeciNum[0]

def strxor(a, b):   # xor two strings of different lengths
    ans = ""
    if len(a) > len(b):
        for x, y in zip(a[:len(b)], b):
            x = hex_to_binary(x)
            y = hex_to_binary(y)
            tmp = ""
            for i in range(4):
                # ans += str(ord(x[i]) - ord('0') ^ ord(y[i]) - ord('0'))
                tmp += str(ord(x[i]) - ord('0') ^ ord(y[i]) - ord('0'))
            tmp = binToHexa(tmp)
            ans += tmp
            # print(x, " xor ", y, " = ", tmp)
        # print(ans)
    else:
        for x, y in zip(a, b[:len(a)]):
            x = hex_to_binary(x)
            y = hex_to_binary(y)
            tmp = ""
            for i in range(4):
                # ans += str(ord(x[i]) - ord('0') ^ ord(y[i]) - ord('0'))
                tmp += str(ord(x[i]) - ord('0') ^ ord(y[i]) - ord('0'))
            tmp = binToHexa(tmp)
            ans += tmp
        
    ans = bytearray.fromhex(ans).decode()
    return ans

print(strxor(key, text))
# scale = 16 ## equals to hexadecimal
# 
# num_of_bits = 8

# bin1 = bin(int(key, scale))[2:].zfill(num_of_bits)
# bin2 = bin(int(text, scale))[2:].zfill(num_of_bits)
# number, pad, rjust, size, kind = key, '0', '>', 42, 'b'
# bin1 = f'{number:{pad}{rjust}{size}b}'
# number, pad, rjust, size, kind = text, '0', '>', 42, 'b'
# bin2 = f'{number:{pad}{rjust}{size}b}'
# print(bin1)
# print(bin2)
# xored = ""
# for i in range(len(bin1)):
    # xored += str(ord(bin1[i]) ^ ord(bin2[i]))
# print(xored)
# 
# ans = bytearray.fromhex(xored).decode()
# print(ans)