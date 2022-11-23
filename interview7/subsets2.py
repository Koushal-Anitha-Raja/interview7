class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #first sort the nums array
        nums.sort()
        
		#then find all subsets:
        combinations = [[]]
        #initially length is one as empty set
        combinations_len = 1
        #iterate through the nums array
        for i in range(len(nums)):
			#if duplicate, start from the new items appended by the previous val
            start = combinations_len if i and nums[i] == nums[i - 1] else 0
			
            combinations_len = len(combinations) 
            #iterate from start to combination length
            for c in range(start, combinations_len):
                #append all the range values in combination array
                combinations.append(combinations[c] + [nums[i]])
         #then return the combination array        
        return combinations