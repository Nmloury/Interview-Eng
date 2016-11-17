def array_left_rotation(a, n, d):
    output = [0 for i in a]
    for i, num in enumerate(a):
        output[i - d] = num
    return output

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
