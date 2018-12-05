data = [int(i) for i in open('input.txt').read().strip().split('\n')]

# Part 1
print(f"Part #1: {sum(data)}")

# Part 2
seen, cumulator = [data[0]],data[0]+data[1]
while cumulator not in seen:
    seen.append(cumulator)
    cumulator+=data[len(seen)%len(data)]
   
print(f"Part #2: {cumulator}")

