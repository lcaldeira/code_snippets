def moving_average(x:np.ndarray, w:int, strategy:str='conv') -> np.ndarray:
  """Moving average of 1D array `x` with sliding window `w`.

  Source: https://stackoverflow.com/questions/14313510/how-to-calculate-rolling-moving-average-using-python-numpy-scipy
  """
  
  assert strategy in ['conv', 'cumsum']
  if strategy == 'conv':
    return np.convolve(x, np.ones(w), 'valid') / w
  elif strategy == 'cumsum':
    ret = np.cumsum(x, dtype=float)
    ret[w:] = ret[w:] - ret[:-w]
    return ret[w - 1:] / w
