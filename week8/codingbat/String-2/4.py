def count_code(str):
  cnt = 0
  for i in range(4, len(str)+1):
    if (str[i-4:i-2] == 'co') & (str[i-1] == 'e'):
      cnt+=1
  return cnt
