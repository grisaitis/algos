from algos.sorting.insertion_sort import insertion_sort
from tests.sorting.base import make_random_list_of_ints


class TestInsertionSort:
  def test_sorts_list_of_length_5(self):
    list_of_ints = make_random_list_of_ints(n=5)
    assert insertion_sort(list_of_ints) == list(range(5))

  def test_sorts_list_of_length_100(self):
    list_of_ints = make_random_list_of_ints(n=100)
    assert insertion_sort(list_of_ints) == list(range(100))
