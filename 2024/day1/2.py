a = []
b = []

line = input()

while line != "":
    line = line.split("   ")
    a.append(int(line[0]))
    b.append(int(line[1]))
    try:
        line = input()
    except EOFError:
        break


similarity = 0

b_count = [0] * 100000

for _ in range(len(b)):
    b_count[b[_]] += 1

for _ in range(len(a)):
    similarity += b_count[a[_]] * a[_]

print(similarity)
