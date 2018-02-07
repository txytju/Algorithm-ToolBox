# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)-1

    while left <= right:
        
        middle = (left + right)//2
        
        if a[middle] == x:
            return middle
        elif a[middle] > x:
            right = middle - 1
        else:
            left = middle + 1
        
    return -1


if __name__ == '__main__':

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end = ' ')




