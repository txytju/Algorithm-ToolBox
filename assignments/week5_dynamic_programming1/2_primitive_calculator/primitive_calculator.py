# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)


def optimal_sequence(n):
    
    # 使得 索引值 就是数字的值 
    # num_operations[0] = num_operations[1] = 0
    num_operations = []
    num_operations.append(0)
    num_operations.append(0)
    
    path_to_number = [[0],[1]]
    
    for i in range(2, n+1):
        
        counts = []
        path = []
        
        if i%2 == 0:
            counts.append(num_operations[int(i/2)] + 1)
            path.append(path_to_number[int(i/2)] +[i])
        if i%3 == 0:
            counts.append(num_operations[int(i/3)] + 1)
            path.append(path_to_number[int(i/3)] + [i])
        counts.append(num_operations[i-1] + 1)
        path.append(path_to_number[i-1] + [i])
        
        num_operations.append(min(counts))
        index = counts.index(num_operations[-1])
        path_to_number.append(path[index])
    
    # return num_operations[n], path_to_number[n]
    return path_to_number[n]

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
