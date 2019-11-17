def insertion_sort(x: list):
  for i_outer, _ in enumerate(x):
    for i_inner, _ in enumerate(x[i_outer + 1:], start=i_outer + 1):
      print(len(x), i_outer, i_inner)
      if x[i_inner] < x[i_outer]:
        x[i_outer], x[i_inner] = x[i_inner], x[i_outer]
  return x
