import random


class TestPythonSort:
  def test_python_sorts_big_list(self):
    big_thing = list(range(10000))
    random.seed(0)
    random.shuffle(big_thing)
    assert list(sorted(big_thing)) == list(range(10000))
