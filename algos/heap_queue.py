import math


class HeapQueue:
  '''
  min-oriented heap
  '''
  def __init__(self):
    self.heap = [None, None]
    self.size = 0

  def _grow_heap(self):
    self.heap = self.heap + list(None for _ in self.heap)

  def _shrink_heap(self):
    new_size = len(self.heap) // 2  # must be integer division for indexing
    self.heap = self.heap[:new_size]

  def __str__(self):
    return "\n".join(
        " ".join(f"{self.heap[i]}" for i in range(2 ** level, 2 ** (level + 1)))
        for level in range(math.ceil(math.log2(self.size)))
    )

  def push(self, item):
    self.size += 1
    if self.size >= len(self.heap) / 2:
      self._grow_heap()
    k = self.size
    self.heap[k] = item
    while k > 1 and self.heap[k] < self.heap[k // 2]:
      self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
      k = k // 2

  def pop(self):
    if self.size == 0:
      return None
    return_value = self.heap[1]
    self.heap[1], self.heap[self.size] = self.heap[self.size], None
    self.size -= 1
    k = 1
    while 2 * k <= self.size:
      if self.heap[2 * k + 1] is None:
        child_k = 2 * k
      else:
        child_k = 2 * k if self.heap[2 * k] < self.heap[2 * k + 1] else 2 * k + 1
      if self.heap[child_k] < self.heap[k]:
        self.heap[k], self.heap[child_k] = self.heap[child_k], self.heap[k]
      k = child_k
    if self.size > 1 and self.size < len(self.heap) / 2:
      self._shrink_heap()
    return return_value

  def peek(self):
    return self.heap[1]
