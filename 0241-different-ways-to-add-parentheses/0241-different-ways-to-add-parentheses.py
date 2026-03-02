class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        

        def helper(expr):
            res = []

            for i in range(len(expr)):
                if expr[i] in "+*-":
                    left = helper(expr[:i])
                    right = helper(expr[i+1:])

                    for l in left:
                        for r in right:
                            if expr[i] == "+":
                                res.append(l+r)
                            elif expr[i] == "-":
                                res.append((l-r))
                            else:
                                res.append(l*r)
            if not res:
                return [int(expr)]
            return res
        return helper(expression)