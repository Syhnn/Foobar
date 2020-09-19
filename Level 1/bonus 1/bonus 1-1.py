braille = ["100000", "110000", "100100", "100110", "100010", "110100", "110110", "110010", "010100", "010110", "101000", "111000", "101100", "101110", "101010", "111100", "111110", "111010", "011100", "011110", "101001", "111001", "010111", "101101", "101111", "101011"]
space = "000000"
marker = "000001"

def solution(s):
  result = ""
  for c in s:
    val = ord(c)
    if val == 32:
      result = result + space
    elif val >= 97 and val <= 122:
      result = result + braille[ord(c) - 97]
    elif val >= 65 and val <= 90:
      result = result + marker
      result = result + braille[ord(c) - 65]
  return result