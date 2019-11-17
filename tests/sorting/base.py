import random


def make_random_list_of_ints(n):
  list_of_ints = list(range(n))
  random.seed(0)
  random.shuffle(list_of_ints)
  return list_of_ints
