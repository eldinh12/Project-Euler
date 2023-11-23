def fibonacci():
    nums = [1, 2]
    total = 2

    while total <= 4000000:
        new_num = nums[len(nums)-1] + nums[len(nums)-2]
        nums.append(new_num)
        if new_num % 2 == 0:
            total += new_num
    return total



print(fibonacci())