class Solution:
    def constructTransformedArray(self, nums: list[int]) -> list[int]:
        """
        Function takes a list as an input (array) and returns another list as an ouput (array).
        Read the problem statement and let me know more about what is needed.
        """
        # Write code to transform array here:
        n= len(nums)
        result = [0] * n
        for i in range(n):
            if nums[i]==0:
                result[i]=nums[i]
            elif nums[i]>0:
                result[i]=nums(i+nums[i])
            else:
                result[i]=nums(i+nums[i])
        return result

        return [] # Returning an empty list for now.

answer = Solution()
transformed_array = answer.constructTransformedArray(nums = [3,-2,1,1])
print(f"Transformed Array: {transformed_array}")
answer.constructTransformedArray()