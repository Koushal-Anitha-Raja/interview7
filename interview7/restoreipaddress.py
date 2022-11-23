class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #path array 
        path = []
        #result array
        result = []
        #a dfs function with path and result
        self.dfs(s, path, result)
        #then return the result
        return result
    
    #the dfs function has string, path and result list 
    def dfs(self, s: str, path: List, result: List):
        #if not string and path length is exactly 4 join it by reversing the path  
        if not s and len(path) == 4:
            s = '.'.join(path[::-1])
            result.append(s)
            return
        #if the path length is 4 return as it should be maximum 3 characters
        elif len(path) == 4:
            return 
        
        else:
            #traverse through 1 to minimum between the 3(it is the maximum possible length of each character) and length of string
            for i in range(1, min(3, len(s))+1):
                #the string range should be from 0 to 255
                if int(s[:i]) >= 0 and int(s[:i]) <= 255:
                    #if the current i value is greater than 1 and initial index is zero continue
                    if i > 1 and s[0]=='0':
                        continue
                    else: 
                        #else call the dfs function with string from starting to end and path is whole string plus path array and result 
                        self.dfs(s[i:], [s[:i]]+path, result)
            return
        