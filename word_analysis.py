# This file contains functions/algorythms to study the frequency of words in a txt file
# and to randomly extract from the set of distinct words, based on the observed frequency.

import string
import time


def remove_punctuation(word):
    import string
    exclude = set(string.punctuation)
    exclude.add(chr(8220))
    exclude.add(chr(8221))
    tmp_w = list(word)
    for ch in tmp_w:
        if ch in exclude:
            tmp_w.remove(ch)
    return ''.join(tmp_w)

# def process_line(line):
#     global wd
#     line.replace('-', ' ')
#     lst_wds_tmp = line.split()
#     for w in lst_wds_tmp:
#             tmp_wd = remove_punctuation(w).lower()
#             if tmp_wd in wd.keys():
#                 wd[tmp_wd] = wd[tmp_wd] + 1
#             else:
#                 wd[tmp_wd] = 1

def process_line(line):
    global wd
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        wd[word] = wd.get(word, 0) + 1


def print_most_common(mydict, N=10, dir='top'):
    # use the dict() wd to print the 10 most used words in the text
    wdt = []
    for word, freq in wd.items():
        wdt.append((freq, word))
    if dir == 'top':
        wdt.sort(reverse=True)          # it sorts on the firsof the two values, so on the frequencies
    else:
        wdt.sort(reverse=False)          # it sorts on the firsof the two values, so on the frequencies
    for freq, word in wdt[0:N]:
        print(str(word) + '\t' + str(freq))


# def inv_search(cumul, k):
#     n = int(len(cumul)/2)
#     step = int(len(cumul) / 2)
#     #print('k = ' + str(k) + '   n = '+str(n))
#     while not(k >= cumul[n-1] and k < cumul[n-1+1]):
#         step = max(int(step/2),1)
#         if k < cumul[n-1]:
#             n = max(n-step,0)
#         else:
#             n = max(n+step,0)
#         #print('k = ' + str(k) + '   n = '+str(n))
#     return n - 1


def inv_search(cumul, k):
    ratio = [abs((a / b) - 1) for a,b in zip(cumul, [k]*len(cumul))]
    n = 0
    minl = []
    for r in ratio:
        minl.append((r, n))
        n += 1
    minl.sort(reverse = False)
    return minl[0][1]

def pic_words_from_text(hist):
    import random
    w = []
    cum = []
    for word, freq in hist.items():
        w.append(word)
        if not cum:
            cum.append(freq)
        else:
            cum.append(cum[-1] + freq)
    #print('max cumul ' + str(cum[-1]))
    r = random.randrange(1, cum[-1]-1, 1)
    n = inv_search(cum, r)
    return w[n]

t0 = time.time()
exclude = set(string.punctuation)
fin = open('test_hist.txt') # open('emma.txt') #open('text_file_generic.txt')
num_lines = 1
wd = dict()
tmp_w = []
for line in fin:
    #if num_lines > 37:
    process_line(line)
    num_lines += 1

t1 = time.time()
# print('Total number of words: ' + str(sum(wd.values())))
# print('Number of distinct words: ' + str(len(wd.keys())))
# print('Time in seconds: ' + str(t1-t0) + '\n')
#print_most_common(wd, 10, 'top')

wlist = []
for i in range(10000):
    wlist.append(pic_words_from_text(wd))

letters = ['a','b','c','d','e', 'f', 'g','h','i','j']
counts = [0]*len(letters)
tmpw = []
n = 0
for h in letters:
    tmpw = [ x for x in wlist if x == h ]
    counts[n] = len(tmpw)
    n += 1
    print(str(h) + ' ' + str(34*len(tmpw)/10000))

