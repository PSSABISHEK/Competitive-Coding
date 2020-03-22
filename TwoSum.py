def TwoSum(nums, target):
    new = []
    for i in nums:
        for j in nums:
            if int(i) + int(j) == target:
                new.append(nums.index(i))
                new.append(nums.index(j))
                return new    

n = []
n = input()
n = n.split()
target = int(input())
print(TwoSum(n, target))