import pytest

from sorting.merge_sort import merge_sort
from tests.sorting.base import make_random_list_of_ints


class TestMergeSort:
  def test_sorts_list_of_length_5(self):
    list_of_ints = make_random_list_of_ints(n=5)
    assert merge_sort(list_of_ints) == list(range(5))

  def test_sorts_list_of_length_10000(self):
    list_of_ints = make_random_list_of_ints(n=10000)
    assert merge_sort(list_of_ints) == list(range(10000))

  @pytest.mark.skip(reason="not implemented")
  def test_is_stable(self):
    pass
