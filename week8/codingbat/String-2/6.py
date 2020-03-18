def xyz_there(str):
  for i in range(3, len(str)+1):
    if str[i-3:i] == 'xyz':
      if str[i-4] == '.':
        continue
      return True
  return False
