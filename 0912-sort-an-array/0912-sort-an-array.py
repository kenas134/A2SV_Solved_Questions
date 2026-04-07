class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left_half,right_half):

            temp = []
            i = 0
            j = 0
            
            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    temp.append(left_half[i])
                    i += 1
                else:
                    temp.append(right_half[j])
                    j += 1
            temp.extend(left_half[i:])
            temp.extend(right_half[j:])
            return temp

        def mergesort(left,right):
            if left == right:
                return [nums[left]]
            elif left > right:
                return []
            mid = (left+right)//2
            left_part = mergesort(left,mid)
            right_part = mergesort(mid+1,right)

            return merge(left_part,right_part)

        return mergesort(0,len(nums)-1)