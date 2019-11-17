from tests.sorting.base import make_random_list_of_ints


class TestPythonSort:
  def test_sorts_list_of_length_10000(self):
    list_of_ints = make_random_list_of_ints(n=10000)
    assert list(sorted(list_of_ints)) == list(range(10000))
