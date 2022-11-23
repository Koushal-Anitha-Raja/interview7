class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #dictionary to store key and value
        memo = {}
        #backtrack function has nums target and i values
        return self.backtrack(nums, 0, target, memo) 
    
    def backtrack(self, nums, i, target, memo):
        #if i and target values in memo dict
        if (i, target) in memo:
            #return both 
            return memo[i, target] 
        #if the i value is lenght of nums
        if i == len(nums): 
            #and target is 0 return 1
            if target == 0: 
                return 1
            else: 
                #orelse return 0
                return 0

            #assign currsum to 0
        curSum = 0 
        #currsum is target-nums[i] values
        curSum += self.backtrack(nums, i+1, target - nums[i], memo) 
         #currsum is target+nums[i] values
        curSum += self.backtrack(nums, i+1, target + nums[i], memo) 
        #currsum is value of dict in i and target
        memo[(i, target)] = curSum 
        return curSum
        