class NumArray:

    def __init__(self, nums):
        self.prefix = []
        total = 0
        for n in nums:
            total += n
            self.prefix.append(total)
        print(self.prefix)
        print(total)

    def sumRange(self, left: int, right: int) -> int:

        preRight = self.prefix[right]
        preLeft = self.prefix[left-1] if left > 0 else 0
        print(f"preRight: {preRight} - {preLeft}")
        return (preRight - preLeft)
nums = [-2,0,3,-5,2,-1]
left = 1
right = 4
obj = NumArray(nums)

param_1 = obj.sumRange(left,right)
print(param_1)