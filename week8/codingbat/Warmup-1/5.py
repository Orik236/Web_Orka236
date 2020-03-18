def parrot_trouble(talking, hour):
  if (talking == True) & ((hour < 7) | (hour > 20)):
    return True
  return False
