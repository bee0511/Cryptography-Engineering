
def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	else:
		g, y, x = egcd(b % a, a)
		return (g, x - (b // a) * y, y)

def modinv(a, b):
    g, x, y = egcd(a, b)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return g, x, y

if __name__=="__main__":
    a, b = 48, 13

    gcd, inv_a, inv_b = modinv(a, b)
    
    print(a, " * ", inv_a, " + ", b, " * ", inv_b, " = ", gcd)
    if inv_b < 0:
        inv_b = inv_b + a
    print("The inverse of 13 is: ", inv_b)