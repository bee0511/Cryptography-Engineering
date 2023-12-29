
from collections import Counter
import numpy as np
ciphertext_bonus ="L L O W A P O L N H N H O E G Y S O K D N D W N I T U I E E F H M D R I E B Y T C W E O H A R R U E"
A_1 = ciphertext_bonus.split() 

vowels = ["A", "E", "I", "O", "U"]
row = 9
column = int(len(A_1) / row) + 1
for i in range(row * column - len(A_1) - 1, 0, -1):
    A_1.insert(-(column - 1) * i, 0)
A_1.append(0)
A_2 = np.reshape(A_1, (row, -1))
for A_row in A_2.tolist():
    print([ch for ch in A_row if ch != "0"])