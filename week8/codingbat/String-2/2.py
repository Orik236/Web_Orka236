def count_hi(str):
  cnt = 0
  for i in range(2, len(str)+1):
    if str[i-2:i] == 'hi':
      cnt+=1
  return cnt
