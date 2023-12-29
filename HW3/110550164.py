import fileinput
import statistics
from collections import deque
def calculate_IC(message):
    alphebets = [0 for i in range(26)]
    for ch in message:
        alphebets[ord(ch) - ord("A")] += 1
    f_sum = 0
    for i in range(26):
        f_sum += alphebets[i] * (alphebets[i] - 1)
        #print(chr(ord("A") + i), ": ", alphebets[i], sep = "")
    return (f_sum / (len(message) * (len(message) - 1)))

def calculate_IC_keys(message, key_size):
    Incidence_of_coincidence = [0 for i in range(key_size)]
    for key_row in range(key_size):
        message_jump = ""
        for i in range(key_row, len(message), key_size):
            message_jump += message[i]
        #print("=======")
        #print(message_jump)
        #print("=======")
        Incidence_of_coincidence[key_row] = calculate_IC(message_jump)
    average_IC = statistics.mean(Incidence_of_coincidence)
    #print("The average IC of the ciphertext is:", average_IC)
    return average_IC

def get_from_stdin():
    message = ""
    for line in fileinput.input():
        if(line == '\n'):
            break
        message += line.rstrip()
    message = ''.join(message.split())
    #print("the ciphertext is:", ciphertext)
    return message

def get_key_size(message, guess_max_key_size):
    max_IC = -1
    for i in range(1, guess_max_key_size + 1):
        IC_keys = calculate_IC_keys(message, i)
        #print(IC_keys)
        if (max_IC < IC_keys):
            max_IC = IC_keys
            key_size = i
    return key_size

def split_with_keysize(message, key_size):
    split_texts = ["" for i in range(key_size)]
    for key_row in range(key_size):
        for i in range(key_row, len(message), key_size):
            split_texts[key_row] += message[i]
    return split_texts

def count_letters(message):
    letters = [0 for i in range(26)]
    for ch in message:
        letters[ord(ch) - ord("A")] += 1
    return letters

def find_chi(letters, split_text):
    letter_happen_rate = [0.082, 0.015, 0.028, 0.043, 0.13,
                      0.022, 0.02, 0.061, 0.07, 0.0015,
                      0.0077, 0.04, 0.024, 0.067, 0.075,
                      0.019, 0.00095, 0.06, 0.063, 0.091, 
                      0.028, 0.0098, 0.024, 0.0015, 0.02, 
                      0.00074]
    letter_expected = [letter_happen_rate[i] * len(split_text) for i in range(26)]
    #print(len(split_text))
    letters = deque(letters)
    min_chi_square = float("inf")
    for j in range(26):
        chi_square = sum([(letters[i] - letter_expected[i]) * (letters[i] - letter_expected[i]) / letter_expected[i] for i in range(26)])
        #print("chi of", chr(j + ord('A')), ":", chi_square)
        if min_chi_square > chi_square:
            key = chr(j + ord('A'))
            min_chi_square = min(min_chi_square, chi_square)
        letters.rotate(-1)
    #print(letters)
    #print(letter_expected)
    #print(chi_square)
    return key
    

def print_chi(split_text, key_size):
    for i in range(key_size):
        print("==============")
        print("chi for the", i,"th key is:")
        letters = count_letters(split_text[i])
        find_chi(letters, split_text[i])
        print("==============")
        
def generate_key(split_text):
    key = ""
    for i in range(len(split_text)):
        letters = count_letters(split_text[i])
        key += find_chi(letters, split_text)
    return key

def restore_with_each_key(message, shift_letter):
    shifted_message =""
    for ch in message:
        #print(ch)
        #print(shift_letter)
        #print(chr((ord(ch) - ord("A") + ord(shift_letter) - ord("A")) % 26 + ord("A")))
        shifted_message += chr((ord(ch) - ord("A") - ord(shift_letter) - ord("A")) % 26 + ord("A"))
        #print(ch)
    #print(shifted_message)
    return shifted_message

def decrypt(split_text, key):
    #print(key[0])
    plain_text = [restore_with_each_key(split_text[i], key[i]) for i in range(len(split_text))]
    return plain_text

def rearrange_plaintext(plain_text):
    rearranged = ""
    for j in range(len(plain_text[0])):
        for i in range(len(plain_text)):
            if (j >= len(plain_text[i])):
                return rearranged
            rearranged += plain_text[i][j]
    return rearranged

ciphertext = get_from_stdin()
guess_max_key_size = 6
key_size = get_key_size(ciphertext, guess_max_key_size)
# print("The key size is:", key_size)
split_text = split_with_keysize(ciphertext, key_size)
#print_chi(split_text, key_size)
key = generate_key(split_text)
# print("The key is:", key)
plain_text = decrypt(split_text, key)
plain_text = rearrange_plaintext(plain_text)
# print("The plaintext is:")
# print(plain_text)

fp = open("message_out.txt", "w")
fp.write(plain_text)
fp.close()