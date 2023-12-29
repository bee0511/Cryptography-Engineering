import hashlib
PASSLIST = [
        'test',
        'name',
        'hello',
        'password',
        'goodbye',
        '12345',
        '123456',
        '123456789',
        'test1'
]
def solve_hash(hash):
    print("Solving hash:", hash)
    for word in PASSLIST:
        guess = hashlib.md5(word.encode('utf-8')).hexdigest()
        if guess.upper() == hash or guess.lower() == hash:
                print(f'[+] Password found: {word}')
                return
        else:
                print(f'[-] Guess: {word} incorrect...')
    print('Password not found in wordlist...')

hash1 = '5f4dcc3b5aa765d61d8327deb882cf99'
hash2 = '5a105e8b9d40e1329780d62ea2265d8a'

solve_hash(hash1)
solve_hash(hash2)