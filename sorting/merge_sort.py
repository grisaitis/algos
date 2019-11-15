def merge_sort(x: list):
  n = len(x)
  def combine(y, z):
    i_y = i_z = 0
    n_y, n_z = len(y), len(z)
    result = list()
    while i_y < n_y and i_z < n_z:
      if y[i_y] < z[i_z]:
        result.append(y[i_y])
        i_y += 1
      else:
        result.append(z[i_z])
        i_z += 1
    result.extend(y[i_y:n_y])
    result.extend(z[i_z:n_z])
    return result

  if n == 1:
    return x
  if n == 2:
    if x[0] > x[1]:
      return x[::-1]  # reverse x
    return x
  midpoint = n // 2
  x1, x2 = x[0:midpoint], x[midpoint:n]
  return combine(merge_sort(x1), merge_sort(x2))
