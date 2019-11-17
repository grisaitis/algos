class HeapQueue(object):
  '''
  min-oriented heap
  '''
  def __init__(self):
    self.heap = [None, None]
    self.size = 0

  def push(self, item):
    self.size += 1
    try:
      self.heap[self.size]
    except IndexError:
      self.heap = self.heap + list(None for _ in self.heap)
    k = self.size
    self.heap[k] = item
    while k > 1 and self.heap[k] < self.heap[k // 2]:
      self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]
      k = k // 2

  def pop(self):
    if self.size == 0:
      return self.heap[1]
    return_value = self.heap[1]
    self.heap[1] = None  # needed for case that size == 1
    self.heap[1] = self.heap[self.size]
    self.size -= 1
    k = 1
    while True:
      if 2 * k > self.size:
        return return_value
      if self.heap[k] > self.heap[2 * k] or self.heap[k] > self.heap[2 * k + 1]:
        if self.heap[2 * k] < self.heap[2 * k + 1]:
          k = 2 * k
        else:
          k = 2 * k + 1
        self.heap[k], self.heap[k // 2] = self.heap[k // 2], self.heap[k]

  def peek(self):
    return self.heap[1]
