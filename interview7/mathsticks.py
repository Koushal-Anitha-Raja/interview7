class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        #there should be at least 4 matchsticks to create square.
        if len(matchsticks) < 4:
            return False
        
        # Sum of matchstick lengths should be divisble by four to form square
        side_length, remainder = divmod(sum(matchsticks), 4)
        #if remainder is not zero it wont create square
        if remainder != 0:
            return False
        
        #single matchstick cannot be greater than side_length.
        if max(matchsticks) > side_length:
            return False
        
        # Check if partitioning is possible.
        return self.can_partition(matchsticks, 4, side_length)
    #partitiing function
    def can_partition(self, nums, k, target):
        #all the buckets value is zero of k length
        buckets = [0] * k
        nums.sort(reverse=True) 
        
        def backtrack(index):
            # If all elements have been used, check if all are equal.
            if index == len(nums):
                return len(set(buckets)) == 1
            
            #placing the values in each bucket
            for b in range(k):
                #adding buckets  
                buckets[b] += nums[index]
                if buckets[b] <= target and backtrack(index + 1):
                    return True
                buckets[b] -= nums[index]
                
                #Buckets are filled from left to right. If any bucket remains empty,
                # then all buckets to the right of it will also be empty.
                if buckets[b] == 0:
                    break
            
            return False
        
        return backtrack(0)