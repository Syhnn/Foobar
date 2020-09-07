def solution(s):
  result = ""
  str = list(s)
  for c in str:
    if c.islower():
      result = result + chr(122 - (ord(c) - 97))
    else:
      result = result + c
  return result

print solution("this is a Random SeNtEnCe !")