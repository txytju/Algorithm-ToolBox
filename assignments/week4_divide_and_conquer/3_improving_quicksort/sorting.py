# Uses python3
import sys
import random

def partition3(a, l, r):

    # 首先保证 a[m1] = pivot & a[i]<a[m1] for i<m1
    x = a[l]
    m1 = l
    for i in range(l+1, r+1):
        if a[i] < x:
            m1 += 1
            a[m1], a[i] = a[i], a[m1]
    a[l], a[m1] = a[m1], a[l]

    # 在 pivot 的后续中寻找与之相等的
    m2 = m1;
    for i in range(m1+1, r+1):
        if a[i] == a[m1]:
            m2 += 1
            a[m2], a[i] = a[i], a[m2]

    # m1 指向 等于 pivot 的最小下标
    # m2 指向 等于 pivot 的最大下标
    return m1, m2

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


# randomized_quick_sort using partition2

# def randomized_quick_sort(a, l, r):
#     if l >= r:
#         return
#     k = random.randint(l, r)
#     a[l], a[k] = a[k], a[l]
#     m = partition2(a, l, r)
#     randomized_quick_sort(a, l, m - 1);
#     randomized_quick_sort(a, m + 1, r);


# randomized_quick_sort using partition3

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);





if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')






        
