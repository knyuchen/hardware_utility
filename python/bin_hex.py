from math import *

# input a number (num) and the number of bits (bits)
# returns a string
def dec_to_bin (num, bits):
   out = ''
   if num < 0:
      num = 2**bits + num
   for i in range(int(bits)):
      current = bits-i-1
      div = 2**current
      bi = int(num/div)
      num = num%div
      out = out+str(bi)
   return out
def bin_to_dec_un (num, bits):
   out = 0
   for i in range (bits):
      out = out + int(num[i])*2**(bits-1-i)
   return out
# input a number (num) and the number of bits (bits)
# returns a string
def dec_to_hex (num, bits):
   out = ''
   if num < 0:
      num = 2**bits + num
#   bits = math.ceil(bits/4)
   bits = ceil(bits/4)
   for i in range(int(bits)):
      current = bits-i-1
      div = 16**current
      bi = int(num/div)
      num = num%div
      if bi == 10:
         out = out + 'A'
      elif bi == 11:
         out = out + 'B'
      elif bi == 12:
         out = out + 'C'
      elif bi == 13:
         out = out + 'D'
      elif bi == 14:
         out = out + 'E'
      elif bi == 15:
         out = out + 'F'
      else:
         out = out+str(bi)
   return out

# addr is binary --> string
def check_len (binary, bits):
   assert len(binary) == bits

def hex_encode (binary):
   if binary == '0000' : return '0'
   elif binary == '0001' : return '1'
   elif binary == '0010' : return '2'
   elif binary == '0011' : return '3'
   elif binary == '0100' : return '4'
   elif binary == '0101' : return '5'
   elif binary == '0110' : return '6'
   elif binary == '0111' : return '7'
   elif binary == '1000' : return '8'
   elif binary == '1001' : return '9'
   elif binary == '1010' : return 'A'
   elif binary == '1011' : return 'B'
   elif binary == '1100' : return 'C'
   elif binary == '1101' : return 'D'
   elif binary == '1110' : return 'E'
   elif binary == '1111' : return 'F'
   return '0'

def bin_to_hex (binary):
   out = ''
   loop = ceil(len(binary)/4)
   sign = binary[0]
   sign_extend = 0
   if len(binary) % 4 != 0:
      sign_extend = 4 - len(binary) % 4
   for i in range(sign_extend):
      if binary[0] == '1':
         binary = '1' + binary
      else :
         binary = '0' + binary
   for i in range(loop):
      top = 4*i
      down = 4*(i+1)
      test = binary[top : down]
      out = out + hex_encode(test) 
   return out
