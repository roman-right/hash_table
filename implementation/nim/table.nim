import nimpy

type LinkedListNode = ref object of PyNimObjectExperimental
  key: int
  value: string
  prev, next: LinkedListNode
  isEmpty: bool

proc newNode(): LinkedListNode =
  new(result)
  result.is_empty = true

proc addValue(self: LinkedListNode, key: int, value: string ) {.exportpy.} =
  if self.isEmpty:
    self.key = key
    self.value = value
    self.isEmpty = false

  elif self.key == key:
    self.value = value

  else:
    if self.next.isNil:
      self.next = newNode()
      self.next.prev = self
    addValue(self.next, key, value)

proc getNode(self: LinkedListNode, key: int): LinkedListNode =
  if self.isEmpty:
    raise newException(KeyError, "No such key found")
  elif self.key == key:
    return self
  elif self.next.isNil:
    raise newException(KeyError, "No such key found")
  else:
    return getNode(self.next, key)

proc getValue(self: LinkedListNode, key: int): string  {.exportpy.} =
  return getNode(self, key).value

proc removeValue(self: LinkedListNode, key: int) {.exportpy.} =
  var node: LinkedListNode = getNode(self, key)
  if node.next == nil:
    if node.prev.isNil:
      node.isEmpty = true
    else:
      node.prev.next = nil
  else:
    if node.prev.isNil:
      node.key = node.next.key
      node.value = node.next.value
      node.next = node.next.next
    else:
      node.prev.next = node.next
      node.next.prev = node.prev

type HashTable = ref object of PyNimObjectExperimental
  size: int
  load: int
  maxLoadFactor: float
  array: seq[LinkedListNode]

proc newTable(size: int, maxLoadFactor: float): HashTable {.exportpy.} =
  new(result)
  result.size = size
  result.load = 0
  result.maxLoadFactor = maxLoadFactor
  result.array = newSeq[LinkedListNode](size)
  for i in 0..size-1:
    var newNode: LinkedListNode = newNode()
    result.array[i] = newNode

proc hash(self: HashTable, key: int): int =
  return cast[int]((key * 2654435761) mod self.size)

proc setItemInternal(self: HashTable, key: int, value: string) =
  var nodeIndex: int = hash(self, key)
  addValue(self.array[nodeIndex], key, value)
  self.load += 1

proc resizeTable(self: HashTable) =
  var newTable: HashTable = newTable(size=self.size * 2,
                                      maxLoadFactor=self.maxLoadFactor)
  for node in self.array:
    if not node.isEmpty:
      var element = node
      while not element.isNil:
        setItemInternal(newTable, element.key, element.value)
        element = element.next

  self.size = newTable.size
  self.load = newTable.load
  self.array = newTable.array

proc loadFactor(self: HashTable): float {.exportpy.} =
  return self.load / self.size

proc setItem(self: HashTable, key: int, value: string) {.exportpy.} =
  setItemInternal(self, key, value)
  if loadFactor(self) >= self.maxLoadFactor:
    resizeTable(self)

proc getItem(self: HashTable, key: int): string {.exportpy.} =
  var node_index: int = hash(self, key)
  return getValue(self.array[node_index], key)

proc delItem(self: HashTable, key: int) {.exportpy.} =
  var node_index: int = hash(self, key)
  removeValue(self.array[node_index], key)
  self.load -= 1

