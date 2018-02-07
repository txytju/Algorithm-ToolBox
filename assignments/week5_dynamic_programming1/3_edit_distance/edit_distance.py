# Uses python3
from numpy import zeros

def edit_distance(s, t):
	n = len(s) + 1
	m = len(t) + 1
	D = zeros((n,m))
	for i in range(n):
		D[i,0] = i
	for j in range(m):
		D[0,j] = j

	for j in range(1,m):
		for i in range(1,n):
			insertion = D[i, j-1] + 1
			deletion = D[i-1, j] + 1
			match = D[i-1, j-1]
			mismatch = D[i-1, j-1] + 1

			if s[i-1] == t[j-1]:
				D[i,j] = min(insertion, deletion, match)
			else:
				D[i,j] = min(insertion, deletion, mismatch)

	return int(D[n-1, m-1])
 




if __name__ == "__main__":
    print(edit_distance(input(), input()))
