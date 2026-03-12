 
s = input()

stack = []
maxx = [0,1]
for i in range(len(s)):
    if s[i] == "(":
        stack.append(i)
    else:
        if stack and s[stack[-1]] == "(":
            stack.pop()
            if not stack:
                cur = -1
            else:
                cur = stack[-1]
            if maxx[0] < i-cur:
                maxx[0] = i-cur
                maxx[1] = 1
            elif maxx[0] == i-cur:
                maxx[1] += 1
        else:
            stack.append(i)


print(*maxx)
            

        
