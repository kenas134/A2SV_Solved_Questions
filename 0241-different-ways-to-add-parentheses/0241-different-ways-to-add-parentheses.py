from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def helper(left, right):
            res = []

            for i in range(left, right + 1):
                if expression[i] in "+*-":
                    left_a = helper(left, i - 1)
                    right_a = helper(i + 1, right)

                    for l in left_a:
                        for r in right_a:
                            if expression[i] == "+":
                                res.append(l + r)
                            elif expression[i] == "-":
                                res.append(l - r)
                            else:
                                res.append(l * r)


            if not res:
                return [int(expression[left:right + 1])]

            return res

        return helper(0, len(expression) - 1)