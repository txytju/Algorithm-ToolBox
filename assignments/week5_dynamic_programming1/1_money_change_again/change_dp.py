# Uses python3
import sys
from math import inf

def get_change(m):
	min_count = []
	min_count.append(0)
	for i in range(1, m+1):
		min_count.append(inf)
		for j in [1,3,4]:
			if i >= j:
				count = min_count[i-j] + 1
				if count < min_count[i]:
					min_count[i] = count
	return min_count[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
