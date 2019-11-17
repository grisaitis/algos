import random

import pytest

from algos.heap_queue import HeapQueue


class TestHeapQueue:
  def test_heap_condition_satisfied(self):
    '''
    heap_queue condition:
    every parent node has a value less than or equal to any of its children
    '''
    heap_queue = HeapQueue()
    random.seed(0)
    for _ in range(10):
      heap_queue.push(random.randint(-100, 100))
    for k in range(2, heap_queue.size + 1):
      print(k, heap_queue.heap[k], heap_queue.heap)
      assert heap_queue.heap[k] >= heap_queue.heap[k // 2]

  @pytest.mark.skip(reason="not implemented")
  def test_heap_grows_exponentially_base_2(self):
    heap_queue = HeapQueue()
    initial_size = heap_queue.size
    for _ in range(initial_size):
      heap_queue.push(1)
    assert heap_queue.size == initial_size
    heap_queue.add(1)
    assert heap_queue.size == initial_size * 2

  # @pytest.mark.skip("not implemented")
  def test_heap_size_is_always_multiple_of_2(self):
    heap_queue = HeapQueue()
    assert heap_queue.size % 2 == 0
    for _ in range(1000):
      heap_queue.push(1)
      assert len(heap_queue.heap) % 2 == 0

  @pytest.mark.skip(reason="not implemented")
  def test_heap_shrinks_exponentially_base_2(self):
    heap_queue = HeapQueue()
    for _ in range(100):
      heap_queue.push(1)
    previous_size = heap_queue.size
    while heap_queue.size > 0:
      heap_queue.pop()
      if heap_queue.size != previous_size:
        assert heap_queue.size == previous_size / 2

  def test_peek(self):
    stuff = list(range(1000))
    random.seed(0)
    random.shuffle(stuff)
    heap_queue = HeapQueue()
    for item in stuff:
      heap_queue.push(item)
    assert heap_queue.peek() == 0

  def test_heap_grows(self):
    heap_queue = HeapQueue()
    heap_queue.push(1)
    len_before = len(heap_queue.heap)
    heap_queue.push(1)
    assert len(heap_queue.heap) > len_before

  # @pytest.mark.skip(reason="not implemented")
  def test_pop(self):
    heap_queue = HeapQueue()
    heap_queue.push(1)
    assert heap_queue.pop() == 1
    assert heap_queue.size == 0
    heap_queue = HeapQueue()
    heap_queue.push(2)
    heap_queue.push(1)
    assert heap_queue.pop() == 1
    assert heap_queue.size == 1
    assert heap_queue.pop() == 2
    assert heap_queue.size == 0
    heap_queue = HeapQueue()
    heap_queue.push(3)
    heap_queue.push(2)
    heap_queue.push(1)
    assert heap_queue.pop() == 1
    assert heap_queue.size == 2
    assert heap_queue.pop() == 2
    assert heap_queue.size == 1
    assert heap_queue.pop() == 3
    assert heap_queue.size == 0
