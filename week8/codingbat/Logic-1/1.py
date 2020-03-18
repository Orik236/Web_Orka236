def cigar_party(cigars, is_weekend):
  return ((cigars >= 40) & (cigars <= 60)) | ((cigars >= 40) & (is_weekend == True))
