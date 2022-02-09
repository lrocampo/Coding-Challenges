# my solution, 500ms runtime
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(0)
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    result[i] += 1
        return result

# solution by Keith, 50ms runtime

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        smaller_count = {}
        for i in range(len(sorted_nums)-1):
            curr_num = sorted_nums[i]
            next_num = sorted_nums[i+1]
            if next_num < curr_num:
                remaining_values = len(sorted_nums)-(i+1)
                smaller_count[curr_num] = remaining_values

        smaller_count[sorted_nums[-1]] = 0

        output = []
        for num in nums:
            output.append(smaller_count[num])
        
        return output