#列表引用与拷贝：对比 l2 = l1 和 l2 = l1.copy()
#使用L2=L1

l1 = [100, 1000, 10, 400, 25, 40, 0]
l2 = l1

l2.sort()

print("l1\tl2")
for i in range(len(l1)):
    print(f"{l1[i]}\t{l2[i]}")




    