import random

import pytest

from algos.heap_queue import HeapQueue


class TestHeapQueue:
  def test_push_preserves_order(self):
    '''
    heap_queue condition:
    every parent node has a value less than or equal to any of its children
    '''
    heap_queue = HeapQueue()
    random.seed(0)
    for _ in range(50):
      heap_queue.push(random.randint(-100, 100))
      for k in range(2, heap_queue.size + 1):
        print(k, heap_queue.heap)
        assert heap_queue.heap[k] >= heap_queue.heap[k // 2]

  def test_pop_preserves_order(self):
    '''
    heap_queue condition:
    every parent node has a value less than or equal to any of its children
    '''
    heap_queue = HeapQueue()
    heap_queue.heap = [None] + list(range(1023))
    heap_queue.size = 1023
    while heap_queue.size > 0:
      for k in range(2, heap_queue.size + 1):
        assert heap_queue.heap[k] >= heap_queue.heap[k // 2]
      heap_queue.pop()

  def test_heap_grows_and_shrinks_multiple_of_2(self):
    heap_queue = HeapQueue()
    for _ in range(1000):
      heap_queue.push(1)
      assert len(heap_queue.heap) % 2 == 0
    for _ in range(1000):
      heap_queue.pop()
      assert len(heap_queue.heap) % 2 == 0

  def test_peek(self):
    heap_queue = HeapQueue()
    unique_thing = object()
    heap_queue.push(unique_thing)
    assert heap_queue.peek() is unique_thing

  def test_pop(self):
    heap_queue = HeapQueue()
    singleton = object()
    heap_queue.push(singleton)
    assert heap_queue.pop() is singleton
    assert heap_queue.size == 0
