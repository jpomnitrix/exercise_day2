i = 1
j = 0
x = 1
y = 0
while i <= 100:
    if i % 2 == 1:
        j += 1
    i += 1
print(j)

for x in range(1, 100):
    if x % 2 == 1:
        y += 1
print(y)

print([ii for ii in range(1, 11) if ii % 2 == 0])

n = 1
s = 0
while n <= 100:
    s += n
    n += 2
print(s)

