# a_float = 3.74659
# limited_float = "{:.2f}".format(a_float)
#
# print(limited_float)

input_line = input("two numbers with space between the two: ")
separated_nums = input_line.split(" ")
n_times = int(separated_nums[0])
denominator = float(separated_nums[1])
total = 0

for i in range(n_times):
    num = float(input("enter the num: "))
    total += round(num * 10)

# print(total)

answer = total/round(denominator*10)
print(answer)
print(type(answer))

if answer % 1 == 0:
    answer = int(answer)
else:
    answer = int(answer + 1)

print(answer)

# v = input().split()
# N = int(v[0])
# K = float(v[1])
#
# total = 0
# for _ in range(N):
#     x = float(input())
#     total += round(x * 10)
#
# ans = int(total / round(K * 10))
# if total % round(K * 10) != 0:
#     ans += 1
# print(ans)