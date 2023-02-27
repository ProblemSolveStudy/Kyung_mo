s = "K1KA5CB7"

alpha = []
result = 0
for i in s:
    if i.isnumeric():
        result += int(i)
    elif i.isalpha():
        alpha.append(i)

alpha.sort()
alpha.append(str(result))

print("".join(alpha))