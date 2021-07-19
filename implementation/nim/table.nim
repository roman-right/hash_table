import nimpy

type LinkedListNode = ref object of PyNimObjectExperimental
  key: int
  value: string
  prev, next: LinkedListNode
  is_empty: bool

proc newNode(): LinkedListNode =
  new(result)
  result.is_empty = true

proc addValue(self: LinkedListNode, key: int, value: string ) {.exportpy.} =
  if self.is_empty:
    self.key = key
    self.value = value
    self.is_empty = false

  elif self.key == key:
    self.value = value

  else:
    if self.next.isNil:
      self.next = newNode()
      self.next.prev = self
    addValue(self.next, key, value)

proc getNode(self: LinkedListNode, key: int): LinkedListNode =
  if self.is_empty:
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
  var found_node: LinkedListNode = getNode(self, key)
  if found_node.next == nil:
    if found_node.prev.isNil:
      found_node.isEmpty = true
    else:
      found_node.prev.next = nil
  else:
    if found_node.prev.isNil:
      found_node.key = found_node.next.key
      found_node.value = found_node.next.value
      found_node.next = found_node.next.next
    else:
      found_node.prev.next = found_node.next
      found_node.next.prev = found_node.prev

type HashTable = ref object of PyNimObjectExperimental
  size: int
  load: int
  max_load_factor: float
  array: seq[LinkedListNode]

proc newTable(size: int, max_load_factor: float): HashTable {.exportpy.} =
  new(result)
  result.size = size
  result.load = 0
  result.max_load_factor = max_load_factor
  result.array = newSeq[LinkedListNode](size)
  for i in 0..size-1:
    var new_node: LinkedListNode = newNode()
    result.array[i] = new_node

proc hash(self: HashTable, key: int): int =
  return cast[int]((key * 2654435761) mod self.size)

proc setItemInternal(self: HashTable, key: int, value: string) =
  var node_index: int = hash(self, key)
  addValue(self.array[node_index], key, value)
  self.load += 1

proc resizeTable(self: HashTable) =
  var newTable: HashTable = newTable(size=self.size * 2,
                                      max_load_factor=self.max_load_factor)
  for node in self.array:
    if not node.is_empty:
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
  if self.load_factor >= self.max_load_factor:
    resizeTable(self)

proc getItem(self: HashTable, key: int): string {.exportpy.} =
  var node_index: int = hash(self, key)
  return getValue(self.array[node_index], key)

proc delItem(self: HashTable, key: int) {.exportpy.} =
  var node_index: int = hash(self, key)
  removeValue(self.array[node_index], key)
  self.load -= 1

