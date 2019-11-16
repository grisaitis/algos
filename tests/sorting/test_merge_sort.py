import random

from sorting.merge_sort import merge_sort


class TestMergeSort:
  def test_sorts_small_list(self):
    stuff = [2, 4, 3, 1]
    assert merge_sort(stuff) == [1, 2, 3, 4]

  def test_sorts_big_list(self):
    big_thing = list(range(10000))
    random.seed(0)
    random.shuffle(big_thing)
    assert merge_sort(big_thing) == list(range(10000))

  def test_is_stable(self):
    pass
