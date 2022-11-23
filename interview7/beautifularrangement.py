class Solution:
    def countArrangement(self, n: int) -> int:
        #initialize the count var to 0
        self.count = 0
        #backtrack function with index and temp array
        self.backtrack(n, 1, [])
        #return count varaible
        return self.count
        

    def backtrack(self, N, index, temp):
        
        #if the length of temp is N 
        if len(temp) == N:
            #then increment the count variable to one
            self.count += 1
            return
        #iterate throught the int variable 
        for i in range(1, N+1):
            #if i is not in varaible and i modulas index is zero and viceversa is zero
            if i not in temp and (i % index == 0 or index % i == 0):
                #then append i to temp array
                #action
                temp.append(i)
                #recurse
                self.backtrack(N, index+1, temp)
                #backtrack
                temp.pop()
        