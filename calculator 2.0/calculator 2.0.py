prluklad = input("Введіть вираз: ")
all_signs = "+-*/"

inside = ""
outside = ""
mode = False
for i in prluklad:
    if i == "(":
        mode = True
        continue
    if i == ")":
        mode = False
        continue
    if mode:
        inside = inside + i
    else:
        outside = outside + i

nums = []
ops = []
num = ""
for i in inside:
    if i in all_signs:
        nums.append(float(num))
        ops.append(i)
        num = ""
    else:
        num = num + i
if num != "":
    nums.append(float(num))

new_nums = [nums[0]]
new_ops = []
for i in range(len(ops)):
    if ops[i] == "*":
        new_nums[-1] = new_nums[-1] * nums[i+1]
    elif ops[i] == "/":
        new_nums[-1] = new_nums[-1] / nums[i+1]
    else:
        new_ops.append(ops[i])
        new_nums.append(nums[i+1])

res_inside = new_nums[0]
for i in range(len(new_ops)):
    if new_ops[i] == "+":
        res_inside = res_inside + new_nums[i+1]
    elif new_ops[i] == "-":
        res_inside = res_inside - new_nums[i+1]

prluklad2 = ""
mode = False
for i in prluklad:
    if i == "(":
        mode = True
        prluklad2 = prluklad2 + str(res_inside)
        continue
    if i == ")":
        mode = False
        continue
    if not mode:
        prluklad2 = prluklad2 + i

nums = []
ops = []
num = ""
for i in prluklad2:
    if i in all_signs:
        nums.append(float(num))
        ops.append(i)
        num = ""
    else:
        num = num + i
if num != "":
    nums.append(float(num))

new_nums = [nums[0]]
new_ops = []
for i in range(len(ops)):
    if ops[i] == "*":
        new_nums[-1] = new_nums[-1] * nums[i+1]
    elif ops[i] == "/":
        new_nums[-1] = new_nums[-1] / nums[i+1]
    else:
        new_ops.append(ops[i])
        new_nums.append(nums[i+1])

res_outside = new_nums[0]
for i in range(len(new_ops)):
    if new_ops[i] == "+":
        res_outside = res_outside + new_nums[i+1]
    elif new_ops[i] == "-":
        res_outside = res_outside - new_nums[i+1]

print("Результат всього виразу:", res_outside)
