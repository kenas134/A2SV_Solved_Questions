class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five += 1
            elif bills[i] == 10 and five > 0:
                five -= 1
                ten += 1
            elif bills[i] == 20 and ten > 0 and five > 0:
                ten -= 1
                five -= 1
            elif bills[i] == 20 and five > 2:
                five -= 3
            else:
                return False
        return True