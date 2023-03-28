import collections
import math
import random
import string

from matplotlib import pyplot as plt

# Практична робота 5
# Варіант 10

results = []
# Тестова послідовність 1
N_sequence = 100
N1 = 10
N0 = N_sequence - N1
list1 = [1] * N1
list0 = [0] * N0
original_sequence_1 = list1 + list0
random.shuffle(original_sequence_1)
original_sequence_1 = "".join(map(str, original_sequence_1))
unique_chars = set(original_sequence_1)
sequence_alphabet_size = len(unique_chars)
Original_sequence_size = len(original_sequence_1) * 8
# Тестова послідовність 2
list1_2 = ['с', 'е', 'в', 'е', 'р', 'и', 'н']
N1_2 = len(list1_2)
N0_2 = N_sequence - N1_2
list0_2 = [0] * N0_2
original_sequence_2 = list1_2 + list0_2
original_sequence_2 = "".join(map(str, original_sequence_2))
unique_chars_2 = set(original_sequence_2)
sequence_alphabet_size = len(unique_chars_2)
Original_sequence_size_2 = len(original_sequence_2) * 8
# Тестова послідовність 3
original_sequence_3 = list1_2 + list0_2
random.shuffle(original_sequence_3)
original_sequence_3 = "".join(map(str, original_sequence_3))
unique_chars_3 = set(original_sequence_3)
sequence_alphabet_size = len(unique_chars_3)
Original_sequence_size_3 = len(original_sequence_3) * 8
# Тестова послідовність 4
letters = ['с', 'е', 'в', 'е', 'р', 'и', 'н', '5', '2', '9']
n_letters = len(letters)
n_repeats = N_sequence // n_letters
remainder = N_sequence % n_letters
list_4 = letters * n_repeats
list_4 += letters[:remainder]
original_sequence_4 = "".join(map(str, list_4))
unique_chars_4 = set(original_sequence_4)
sequence_alphabet_size = len(unique_chars_4)
Original_sequence_size_4 = len(original_sequence_4) * 8
# Тестова послідовність 5
list_5 = ['с', 'е', '5', '2', '9']
Pi = 0.2
leng = Pi * N_sequence
original_sequence_5 = list_5 * int(leng)
random.shuffle(original_sequence_5)
original_sequence_5 = "".join(map(str, original_sequence_5))
unique_chars_5 = set(original_sequence_5)
sequence_alphabet_size = len(unique_chars_5)
Original_sequence_size_5 = len(original_sequence_5) * 8
# Тестова послідовність 6
letters = ['с', 'е']
digits = ['5', '2', '9']
list_100 = []
Pl = 0.7
Pd = 0.3
n_letters = int(Pl * N_sequence)
n_digits = int(Pd * N_sequence)
for i in range(n_letters):
    list_100.append(random.choice(letters))
for i in range(n_digits):
    list_100.append(random.choice(digits))
random.shuffle(list_100)
original_sequence_6 = "".join(map(str, list_100))
unique_chars_6 = set(original_sequence_6)
sequence_alphabet_size = len(unique_chars_6)
Original_sequence_size_6 = len(original_sequence_6) * 8
# Тестова послідовність 7
elements = string.ascii_lowercase + string.digits
list_100_7 = [random.choice(elements) for i in range(N_sequence)]
original_sequence_7 = "".join(map(str, list_100_7))
unique_chars_7 = set(original_sequence_7)
sequence_alphabet_size = len(unique_chars_7)
Original_sequence_size_7 = len(original_sequence_7) * 8
# Тестова послідовність 8
row8 = ['1'] * N_sequence
original_sequence_8 = "".join(map(str, row8))
unique_chars_8 = set(original_sequence_8)
sequence_alphabet_size = len(unique_chars_8)
Original_sequence_size_8 = len(original_sequence_8) * 8

sequences = open('sequence.txt', 'a')
original_sequences = [original_sequence_1, original_sequence_2,
                      original_sequence_3, original_sequence_4,
                      original_sequence_5, original_sequence_6,
                      original_sequence_7, original_sequence_8]
sequences.write(str(original_sequences))
sequences.close()

for sequence in original_sequences:
    counts = collections.Counter(sequence)
    probability = {symbol: count / N_sequence for symbol, count in counts.items()}
    mean_probability = sum(probability.values()) / len(probability)
    equal = all(abs(prob - mean_probability) < 0.05 * mean_probability for prob in probability.values())
    if equal:
        uniformity = "рівна"
    else:
        uniformity = "нерівна"
    entropy = -sum(p * math.log2(p) for p in probability.values())
    sequence_alphabet_size = len(set(sequence))
    if sequence_alphabet_size > 1:
        source_excess = 1 - entropy / math.log2(sequence_alphabet_size)
    else:
        source_excess = 1

    probability_str = ', '.join([f"{symbol}={prob:.4f}" for symbol, prob in probability.items()])
    with open("results_sequence.txt", "a") as s_file:
        s_file.write(f"Послідовність:  {sequence}\n")
        s_file.write(f"Розмір алфавіту:  {sequence_alphabet_size}\n")
        s_file.write(f"Розмір послідовності:  {Original_sequence_size_8} bits\n")
        s_file.write("Ймовірності появи символів  " + str(probability_str) + "\n")
        s_file.write("Середнє арифметичне ймовірностей  " + str(mean_probability) + "\n")
        s_file.write("Ймовірність розподілу символів  " + str(equal) + "\n")
        s_file.write("Ентропія  " + str(entropy) + "\n")
        s_file.write("Надмірність джерела  " + str(source_excess) + "\n")
        s_file.write("..............................." + "\n")
        results.append([sequence_alphabet_size, round((entropy), 2), round((source_excess), 2), uniformity])

fig, ax = plt.subplots(figsize=(14/1.54, 8/1.54))
headers = ['Розмір алфавіту', 'Ентропія', 'Надмірність', 'Ймовірність']
row = ['Послідовність 1', 'Послідовність 2',
       'Послідовність 3', 'Послідовність 4',
       'Послідовність 5', 'Послідовність 6',
       'Послідовність 7', 'Послідовність 8']
ax.axis('off')
table = ax.table(cellText=results, colLabels=headers, rowLabels=row, loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(0.8, 2)
fig.savefig("Характеристики сформованих послідовностей" + ".png")
