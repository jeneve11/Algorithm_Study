N = int(input())

target = ''
for _ in range(len(bin(N)) - 2):
    target += '1'


if '0' not in str(bin(N))[2:]:
    print(1)
    print(N)

else:
    print(2)
    print(int(target, 2) - N)
    print(N)