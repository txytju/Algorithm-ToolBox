# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = []
    dic = {}
    for i in range(len(starts)):
        for j in range(starts[i],ends[i]+1):
            if j not in dic.keys():
                dic[j] = 1
            else:
                dic[j] += 1

    cnt = [dic[i] if i in dic else 0 for i in points]
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
