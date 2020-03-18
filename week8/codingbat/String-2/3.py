def cat_dog(str):
  cnt_cat = 0
  cnt_dog = 0
  for i in range(3, len(str)+1):
    if str[i-3:i] == 'cat':
      cnt_cat+=1
    elif str[i-3:i] == 'dog':
      cnt_dog+=1
  return cnt_cat==cnt_dog