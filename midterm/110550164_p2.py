def str_to_int(s):
    return int(s.encode().hex(), 16)

if __name__=="__main__":
    message = 0x09e1c5f70a65ac519458e7e53f36
    
    key = str_to_int("attack at dawn") ^ message
    
    print("The one-time pad encryption of the message \"attack at dusk\" under the same OTP key is:")
    print(hex(str_to_int("attack at dusk") ^ key))