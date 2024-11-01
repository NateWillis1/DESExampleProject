# -*- coding: utf-8 -*-
"""DES.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sh5i4c7zZQzswEg0Kh74dXd0ams1pXtr
"""

# Global Variables
hex_key = '133457799bbcdff1'

PC1 = [57,49,41,33,25,17,9,1,58,50,42,34,26,18,10,2,59,51,43,35,27,19,11,3,60,
       52,44,36,63,55,47,39,31,23,15,7,62,54,46,38,30,22,14,6,61,53,45,37,29,21,
       13,5,28,20,21,4]

CircularShift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

PC2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26, 8,16,7,27,20,13,2,41,52,
       31,37, 47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]

IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,62,54,46,38,30,22,14,6,64,
      56,48,40,32,24,16,8,57,49,41,33,25,17,9,1,59,51,43,35,27,19,11,3,61,53,45,
      37,29,21,13,5,63,55,47,39,31,23,15,7]

Ebit = [32,1,2,3,4,5,4,5,6,7,8,9,8,9,10,11,12,13,12,13,14,15,16,17,16,17,18,19,
        20,21,20,21,22,23,24,25,24,25,26,27,28,29,28,29,30,31,32,1]

S1 = [[14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7],
     [0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8],
     [4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0],
     [15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]]

S2 = [[15,1,8,14,6,11,3,4,9,7,2,13,12,0,5, 10],
     [3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5],
     [0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15],
     [13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]]

S3 = [[10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8],
     [13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1],
     [13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7],
     [1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]]

S4 = [[7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15],
     [13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9],
     [10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4],
     [3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]]

S5 = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
      [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
      [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
      [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

S6 = [[12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11],
      [10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8],
      [9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6],
      [4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]]

S7 = [[4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1],
      [13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6],
      [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2],
      [6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]]

S8 = [[13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7],
     [1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2],
     [7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8],
     [2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]]

Slist = [S1,S2,S3,S4,S5,S6,S7,S8]

P = [16,7,20,21,29,12,28,17,1,15,23,26,5,18,31,
     10,2,8,24,14,32,27,3,9,19,13,30,6,22,11,4,25]

IPPowNeg1 = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,38,6,46,14,54,22,62,
             30,37,5,45,13,53,21,61,29,36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,
             27,34,2,42,10,50,18,58,26,33,1,41,9,49,17,57,25]

# Splits a list or string every nth number of characters
def split_every_nth(s,n):
    return [s[i:i+n] for i in range(0,len(s),n)]

# Converts ascii characters to there hex equivalent
def ascii_to_hex(a):
  return [hex(ord(c)).replace('0x','').zfill(2) for c in a]

# Converts hex to ascii
def hex_to_ascii(a):
  return [chr(int(c,16)) for c in a]

# Converts hex to binary
def hex_to_bin(a):
   return "{0:08b}".format(int(a, 16))

# Converts bin to hex
def bin_to_hex(a):
  return hex(int(a,2)).replace('0x','').zfill(2)

# Permutates on tables
def permutate(binval, tab):
  p = ''
  for index in range(len(tab)):
    p += binval[tab[index]-1]
  return p

# Generates binary key
def generate_K(hex_key):
  hex_key = split_every_nth(hex_key,2)
  K = ''.join(hex_to_bin(c) for c in hex_key)
  return K

# Splits two vals
def split(val):
  return val[:len(val)//2], val[len(val)//2:]

# Circular shifts the lists
def circular_shift(val, CircularShift):
  Rlist = []
  Rlist.append(val[CircularShift[0]:] + val[:CircularShift[0]])
  for i in range(1,len(CircularShift)):
    Rlist.append(Rlist[i-1][CircularShift[i]:] + Rlist[i-1][:CircularShift[i]])
  return Rlist

# Combines 2 lists and puts them in a list
def combine_vals(listA, listB):
  CD = []
  for i in range(len(listA)):
    CD.append(listA[i] + listB[i])
  return CD

# Permutates on lists of tables
def permutate_list(binvallist, tab):
  p = []
  for i in range(len(binvallist)):
    p.append(permutate(binvallist[i], tab))
  return p

# Binary Addition using xor
def bin_xor(val1, val2):
  xor = ''
  for i in range(len(val1)):
    if val1[i] == val2[i]:
      xor += '0'
    else:
      xor += '1'
  return xor

def generate_keys(hex_key, PC1, CircularShift, PC2):
  Clist = []
  Dlist = []

  K = generate_K(hex_key)
  Kplus = permutate(K, PC1)
  C0, D0 = split(Kplus)
  CList = circular_shift(C0, CircularShift)
  DList = circular_shift(D0, CircularShift)
  CDList = combine_vals(CList, DList)
  Klist = permutate_list(CDList, PC2)
  return Klist

def SB(BList, STable, P):
  sList = []
  for i in range(len(BList)):
    row = int(BList[i][0] + BList[i][5],2)
    col = int(BList[i][1:5],2)
    S = STable[i][row][col]
    S = '{:0<4}'.format(bin(S).replace('0b',''))
    sList.append(S)
  return permutate(''.join(sList), P)

def perm_and_divi(pText):
  hp_text = ascii_to_hex(pText)
  bp_text = ''.join([hex_to_bin(c) for c in hp_text])
  permutated_text = permutate(bp_text, IP)
  L0, R0 = split(permutated_text)
  return L0, R0

def sixteen_rounds(Klist,L,R):
  Llist = []
  Rlist = []
  #L1 == R0
  Llist.append(R)
  for i in range(16):
    fRK = SB(split_every_nth(bin_xor(permutate(Llist[i],Ebit),Klist[i]),6),Slist,P)
    if i == 0:
      Rlist.append(bin_xor(L,fRK))
    else:
      Rlist.append(bin_xor(Llist[i-1],fRK))
    Llist.append(Rlist[i])
  L = Llist[15]
  R = Rlist[15]
  return L,R

def rev_then_perm(L,R):
  return permutate(R+L,IPPowNeg1)

def encrypt(pText):
  #1st Generate Keys
  Klist = generate_keys(hex_key, PC1, CircularShift, PC2)
  #2nd Permutation and Division
  L0, R0 = perm_and_divi(pText)
  #3rd 16 Rounds
  L16, R16 = sixteen_rounds(Klist,L0,R0)
  #4th Permutation
  CTIB = rev_then_perm(L16,R16)
  CTIH = [bin_to_hex(c) for c in split_every_nth(CTIB,8)]
  CTIA = hex_to_ascii(CTIH)

  return CTIB, CTIH, CTIA

def decrypt(cipher):
  #1st Generate Keys
  Klist = generate_keys(hex_key, PC1, CircularShift, PC2)
  # Reverse List!
  rKlist = Klist[::-1]
  #2nd Permutation and Division
  L0, R0 = perm_and_divi(cipher)
  #3rd 16 Rounds
  L16, R16 = sixteen_rounds(rKlist,L0,R0)
  #4th Permutation
  PTIB = rev_then_perm(L16,R16)
  PTIH = [bin_to_hex(c) for c in split_every_nth(PTIB,8)]
  PTIA = hex_to_ascii(PTIH)

  return PTIB, PTIH, PTIA

p_text = split_every_nth(input("Please input a message for encryption: "),8)
p_text = [a.ljust(8) for a in p_text]

print(p_text)

PITAs = ''

for i in range(len(p_text)):
  print('Plain Text: ',p_text[i])
  CTIB, CTIH, CTIA = encrypt(p_text[i])
  print('Cipher in Binary: \n',CTIB)
  print('Cipher in Hex: \n',CTIH)
  print('Cipher in ASCII: \n',CTIA)

  PTIB, PTIH, PTIA = decrypt(CTIA)
  print('Plain Text in Binary: \n',PTIB)
  print('Plain Text in Hex: \n',PTIH)
  print('Pleain Text in ASCII: \n',''.join(PTIA), '\n')
  PITAs = PITAs + (''.join(PTIA))

print('Final Plain Text: ',PITAs)