prl = input("Enter: ").replace(" ", "")

def fun(prl):
    nums = []
    ops = []
    num = ""
    
    i = 0
    while i < len(prl):
        if prl[i] in "+-*/":
            if num:
                nums.append(float(num))
                num = ""
            ops.append(prl[i])
            i += 1
        elif prl[i] == "(":
            count = 1
            j = i + 1
            while j < len(prl) and count > 0:
                if prl[j] == "(":
                    count += 1
                elif prl[j] == ")":
                    count -= 1
                j += 1
            if count == 0:
                sub_prl = prl[i+1:j-1]
                sub_result = fun(sub_prl)
                nums.append(sub_result)
            i = j
        else:
            num += prl[i]
            i += 1
    
    if num:
        nums.append(float(num))
    
    i = 0
    while i < len(ops):
        if ops[i] == "*":
            nums[i] = nums[i] * nums[i+1]
            del nums[i+1]
            del ops[i]
        elif ops[i] == "/":
            nums[i] = nums[i] / nums[i+1]
            del nums[i+1]
            del ops[i]
        else:
            i += 1
    
    res = nums[0]
    for i in range(len(ops)):
        if ops[i] == "+":
            res += nums[i+1]
        elif ops[i] == "-":
            res -= nums[i+1]
    return res

print("Result:",fun(prl))