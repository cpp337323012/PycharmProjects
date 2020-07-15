'''
冒泡排序

nums = [12, 23, 1, 9]
'''

nums = [12, 23, 1, 9, 4, 3]
for i in range(len(nums)-1):
    print('i:',i)
    for j in range(len(nums)-i-1):
        print('j:', j)
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
        print('第' + str(j) + '次内循环' + str(nums))
    print('第' + str(j) + '次外循环' + str(nums))
print(str(nums))

