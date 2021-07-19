from implementation.py.table import HashTable

ht = HashTable(max_load_factor=0.5)
ht[1] = "test1"
ht[2] = "test2"
ht[3] = "test3"
ht[3] = "test3_1"
ht[4] = "test4"

print(
    ht[1],
    ht[2],
    ht[3],
    ht[4],
)

print(ht.load_factor)
del ht[1]
print(ht.load_factor)
