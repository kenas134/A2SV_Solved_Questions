class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for i in arr:
            if i == "..":
                if stack:
                    stack.pop()
            elif i == "" or i == ".":
                continue
            else:
                stack.append(i)

        print(stack)

        return "/" + "/".join(stack)


