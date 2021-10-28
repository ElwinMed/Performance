files_name = str(input())
f1 = open('%s'%files_name, 'r')
nums = []
for i in f1:
	nums.append(int(i))
f1.close()
n = len(nums)
index = n // 2
nums.sort()
summary = 0
for i in range(len(nums)):
	if i != index:
		summary += abs(nums[i]-nums[index])
print(summary)