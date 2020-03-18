def close_far(a, b, c):
    return ((abs(a - c) <= 1) & (abs(a - b) >= 2) & (abs(c - b) >= 2)) | ((abs(a - b) <= 1) &
                                                                          (abs(a - c) >= 2) & (abs(b - c) >= 2))

