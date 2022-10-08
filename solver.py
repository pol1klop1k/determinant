r = int(input())
num = [[] for k in range(r+1)]
for k in range(1,r+1):
    num[k].append('')
    for n in range(r):
        num[k].append(input())

def alDop(i,j):
    new = [[]]
    for k in range(1,r+1):
        print(k, j)
        if k == i:
            continue
        else:
            new.append(num[k])
            new[k][j] = 0
    return new

print(alDop(2,2))
