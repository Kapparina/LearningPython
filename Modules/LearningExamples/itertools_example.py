import itertools

lst = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(lst)
print(list(sum_list))

lst2 = ["A", "B", "C", "D"]
chain_list = itertools.chain(lst, lst2)
print(list(chain_list))