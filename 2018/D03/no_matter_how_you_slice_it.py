data = open('input.txt').read().split('\n')[:-1]

claims, x, y, l, b = list(zip(*[(i[0], *i[2].split(','), *i[3].split('x')) for i in [i.split(' ') for i in data]]))
y = [int(i.strip(':')) for i in y]
claims = [int(i.strip('#')) for i in claims]
x = list(map(int, x))
l = list(map(int, l))
b = list(map(int, b))

matrix_length = max([i+j for i, j in zip(x, l)])
matrix_width =  max([i+j for i, j in zip(y, b)])

matrix = [[0 for i in range(matrix_width)] for j in range(matrix_length)]

for _x, _y, _l, _b, claim in zip(x,y,l,b,claims):
    for i in range(_l):
            for j in range(_b):
                if matrix[_x+i][_y+j] == 0:
                   matrix[_x+i][_y+j] = claim
                else:
                    matrix[_x+i][_y+j] = -1

# Part 1
count = sum(1 for j in matrix for i in j if i==-1 ) 
print(f"Part #1: {count}")

# Part 2
for _x, _y, _l, _b, claim in zip(x,y,l,b,claims):
    claim_size = _l * _b
    claim_count = 0
    for i in range(_l):
            for j in range(_b):
                if matrix[_x+i][_y+j] == claim:
                  claim_count += 1 
    if claim_count == claim_size:
        print(f"Full claimed {claim}")
        



