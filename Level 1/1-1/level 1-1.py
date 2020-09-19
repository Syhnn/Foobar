def solution(s):
  result = ""
  str = list(s)
  for c in str:
    if c.islower():
      # if char is lowercase its ascii value is between 97 and 122 included, just swap that
      result = result + chr(122 - (ord(c) - 97))
    else:
      result = result + c
  return result

print solution("this is a Random SeNtEnCe !")