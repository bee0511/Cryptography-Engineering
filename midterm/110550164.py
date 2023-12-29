import string
from itertools import combinations
from collections import defaultdict



def problem1():
	CIPHERTEXTS = [
	bytes.fromhex("315c4eeaa8b5f8aaf9174145bf43e1784b8fa00dc71d885a804e5ee9fa40b16349c146fb778cdf2d3aff021dfff5b403b510d0d0455468aeb98622b137dae857553ccd8883a7bc37520e06e515d22c954eba50"),
	bytes.fromhex("234c02ecbbfbafa3ed18510abd11fa724fcda2018a1a8342cf064bbde548b12b07df44ba7191d9606ef4081ffde5ad46a5069d9f7f543bedb9c861bf29c7e205132eda9382b0bc2c5c4b45f919cf3a9f1cb741"),
	bytes.fromhex("32510ba9a7b2bba9b8005d43a304b5714cc0bb0c8a34884dd91304b8ad40b62b07df44ba6e9d8a2368e51d04e0e7b207b70b9b8261112bacb6c866a232dfe257527dc29398f5f3251a0d47e503c66e935de812"),
	bytes.fromhex("32510ba9aab2a8a4fd06414fb517b5605cc0aa0dc91a8908c2064ba8ad5ea06a029056f47a8ad3306ef5021eafe1ac01a81197847a5c68a1b78769a37bc8f4575432c198ccb4ef63590256e305cd3a9544ee41"),
	bytes.fromhex("3f561ba9adb4b6ebec54424ba317b564418fac0dd35f8c08d31a1fe9e24fe56808c213f17c81d9607cee021dafe1e001b21ade877a5e68bea88d61b93ac5ee0d562e8e9582f5ef375f0a4ae20ed86e935de812"),
	bytes.fromhex("32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd2061bbde24eb76a19d84aba34d8de287be84d07e7e9a30ee714979c7e1123a8bd9822a33ecaf512472e8e8f8db3f9635c1949e640c621854eba0d"),
	bytes.fromhex("32510bfbacfbb9befd54415da243e1695ecabd58c519cd4bd90f1fa6ea5ba47b01c909ba7696cf606ef40c04afe1ac0aa8148dd066592ded9f8774b529c7ea125d298e8883f5e9305f4b44f915cb2bd05af513"),
	bytes.fromhex("315c4eeaa8b5f8bffd11155ea506b56041c6a00c8a08854dd21a4bbde54ce56801d943ba708b8a3574f40c00fff9e00fa1439fd0654327a3bfc860b92f89ee04132ecb9298f5fd2d5e4b45e40ecc3b9d59e941"),
	bytes.fromhex("271946f9bbb2aeadec111841a81abc300ecaa01bd8069d5cc91005e9fe4aad6e04d513e96d99de2569bc5e50eeeca709b50a8a987f4264edb6896fb537d0a716132ddc938fb0f836480e06ed0fcd6e9759f404"),
	bytes.fromhex("466d06ece998b7a2fb1d464fed2ced7641ddaa3cc31c9941cf110abbf409ed39598005b3399ccfafb61d0315fca0a314be138a9f32503bedac8067f03adbf3575c3b8edc9ba7f537530541ab0f9f3cd04ff50d"),
	bytes.fromhex("32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904"),  # <- target
	]

	def possible_xor_results(s: str) -> defaultdict[int, list[tuple[int, int]]]:
		charset = [ord(c) for c in s]
		res = defaultdict(list)
		for a, b in combinations(charset, r=2):
			res[a ^ b] += [(a, b)]
		res[0] = [(a, a) for a in charset]
		return res
	possible_xor_pairs = possible_xor_results(string.ascii_letters + " ")

	possible_keys = [defaultdict(int) for _ in range(len(CIPHERTEXTS[0]))]
	for c1, c2 in combinations(CIPHERTEXTS, r=2):
		for keys, b1, b2 in zip(possible_keys, c1, c2):
			possible_cipher_chars = set()
			for x,y in possible_xor_pairs[b1^b2]:
				possible_cipher_chars |= {b1^x, b1^y}
			for c in possible_cipher_chars:
				keys[c] += 1

  # guess the cipher byte that was possible in the most ciphertext pairs
	key_guess = [max(keys, key=keys.get) for keys in possible_keys]
	for i, cs in enumerate(CIPHERTEXTS):
		plaintext_guess = ''.join(chr(x ^ k) for x, k in zip(cs, key_guess))
		print(str(i+1).ljust(2), "|", plaintext_guess)
	print('\n'"The plaintext is: ")
	print("The secret message is: When using a stream cipher, never use the key more than once")
 
def problem2():
	def str_to_int(s):
		return int(s.encode().hex(), 16)
	key = str_to_int("attack at dawn") ^ 0x09e1c5f70a65ac519458e7e53f36
	print("The one-time pad encryption of the message \"attack at dusk\" under the same OTP key is:")
	print(hex(str_to_int("attack at dusk") ^ key))

def problem8():
	a, b = 48, 13
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
	gcd, inv_a, inv_b = modinv(a, b)
	print(a, " * ", inv_a, " + ", b, " * ", inv_b, " = ", gcd)
	print("The inverse of 13 is: ", inv_b)

if __name__=="__main__":
	print("====== Problem 1 ======"'\n')
	problem1()
	print('\n'"====== Problem 2 ======"'\n')
	problem2()
	print('\n'"====== Problem 8 ======"'\n')
	problem8()