---
theme: main 
paginate: true 
backgroundColor: #fff

marp: true
---

## Hash Table

---

![bg 80%](images/hash_table.png)

---

## Hash functions

```python

    def hash(key: int, size: int) -> int:
        return key * 2654435761 % size

```

---

## Load factor

```python
    @property
    def load_factor(self):
        return self.load / self.size
```

`self.load` - Number of stored items
`self.size` - Size of the table

---

## Types of hash tables by collision resolution

- Separate chaining
- Open addressing

---

## Separate chaining 

---

![bg 80%](images/separate_chaining.png)

---

## Opean addressing

---

![bg 80%](images/open_addressing.png)

---

## Resizing

- All-at-once
- Incremental
- Distribited hash tables hashing
- and etc.

---

## Performance

- Search: 
  - Average O(1)
  - Worst O(n)
- Insert
  - Average O(1)
  - Worst O(n)
- Delete
  - Average O(1)
  - Worst O(n)

---

## Implementation

<https://github.com/roman-right/hash_table/tree/main/implementation>

---

## Results

- Load = 1 000 000
- Max load factor = **100**
- Initial table size = 20000

![bg right:50% 80%](images/res_1.png)

---

## Results

- Load = 1 000 000
- Max load factor = **10**
- Initial table size = 20000

![bg right:50% 80%](images/res_2.png)

---

## Results

- Load = 1 000 000
- Max load factor = **1**
- Initial table size = 20000

![bg right:50% 80%](images/res_3.png)

---

## Results

- Load = 1 000 000
- Max load factor = **0.5**
- Initial table size = 20000

![bg right:50% 80%](images/res_4.png)

---

## Pros and Cons

Pros 

- Speed

Cons

- Resizing
- Collisions