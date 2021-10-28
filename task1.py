n = int(input())
m = int(input())
a = [j+1 for j in range(n)]
answer = []
helper, i, k = 0, 0, 0
while i!=0 or helper >=0:
	answer += str(a[i])
	helper -= 1
	if i + m > n :
		i = m - (n - i) - 1
	else:
		i = i + m -1
print(''.join(str(l) for l in answer))
