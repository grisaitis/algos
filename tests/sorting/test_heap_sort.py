import random

import pytest

from algos.heap_queue import HeapQueue


class TestHeapSort:
  @pytest.mark.skip("still working on HeapQueue.pop()")
  def test_sorts_list_of_length_10000(self):
    stuff = list(range(10000))
    random.shuffle(stuff)
    heap_queue = HeapQueue()
    for item in stuff:
      heap_queue.push(item)
    sorted_stuff = list(heap_queue.pop() for _ in range(heap_queue.size))
    assert sorted_stuff == list(range(10000))
