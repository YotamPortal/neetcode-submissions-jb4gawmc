class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        set_res = list()
        nums.sort()

        for i in range(len(nums)):

            # Step 2: Skip the same number to avoid duplicate triplets starting with the same value
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Step 3: Two-pointer search for the remaining two numbers    
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                currentSum = nums[l] + nums[r]
                if currentSum < target:
                    l += 1
                elif currentSum > target:
                    r -= 1
                else:
                    set_res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # Step 4: Skip duplicates for the left pointer to avoid identical triplets
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return set_res
            